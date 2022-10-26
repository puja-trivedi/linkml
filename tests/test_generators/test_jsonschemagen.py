import json
import logging
import unittest

import jsonschema
import yaml
from linkml_runtime.dumpers import json_dumper
from linkml_runtime.loaders import yaml_loader

from linkml.generators.jsonschemagen import JsonSchemaGenerator
from tests.test_generators.environment import env
from tests.test_generators.test_pythongen import make_python

SCHEMA = env.input_path("kitchen_sink.yaml")
DATA = env.input_path("kitchen_sink_inst_01.yaml")
COMPLIANCE_CASES = env.input_path("kitchen_sink_compliance_inst_01.yaml")


class JsonSchemaTestCase(unittest.TestCase):
    """
    Tests generation of JSON-Schema
    """

    def setUp(self):
        generator = JsonSchemaGenerator(
            SCHEMA, 
            mergeimports=True, 
            top_class="Dataset", 
            not_closed=False
        )
        self.kitchen_sink_json_schema = json.loads(generator.serialize())

        generator.not_closed = True
        self.kitchen_sink_json_schema_not_closed = json.loads(generator.serialize())


    def test_jsonschema_integration(self):
        """Integration test for JsonSchemaGenerator.
        
        This test loads an instance object adhering to the kitchen sink schema from
        a YAML file (input/kitchen_sink_inst_01.yaml), performs sanity checks on the
        instance data, constructs a JsonSchemaGenerator from the kitchen sink schema, 
        and uses the jsonschema library to verify that the generated JSON Schema is 
        able to validate the instance data.
        """

        kitchen_module = make_python(False)
        inst: Dataset
        inst = yaml_loader.load(DATA, target_class=kitchen_module.Dataset)
        # p = [p for p in persons if p.id == 'P:002'][0]
        ok_address = False
        ok_history = False
        ok_metadata = True
        for p in inst.persons:
            for a in p.addresses:
                logging.debug(f"{p.id} address = {a.street}")
                if a.street.startswith("1 foo"):
                    ok_address = True
            for h in p.has_medical_history:
                logging.debug(f"{p.id} history = {h}")
                if h.in_location == "GEO:1234" and h.diagnosis.name == "headache":
                    ok_history = True
                # test the metadata slot, which has an unconstrained range
                if h.metadata:
                    if h.metadata.anything.goes:
                        ok_metadata = True
        assert ok_address
        assert ok_history

        json_instance = json.loads(json_dumper.dumps(inst))
        del json_instance['@type']

        jsonschema.validate(json_instance, self.kitchen_sink_json_schema)
        

    def test_class_uri_any(self):
        """Test that class_ur: linkml:Any results in a JSON Schema with 
        "additionalProperties": true.
        
        See also https://github.com/linkml/linkml/issues/579
        """

        self.assertIn("$defs", self.kitchen_sink_json_schema)
        self.assertTrue(self.kitchen_sink_json_schema["$defs"]["AnyObject"]["additionalProperties"])


    def test_compliance_cases(self):
        """Tests various validation compliance cases.

        The file input/kitchen_sink_compliance_inst_01.yaml has multiple documents describing various
        compliance test cases. Minimally each document contains a `dataset` object which will be
        validated against the kitchen sink schema. By default each instance is expected to *fail*
        validation, but cases can also be marked with valid: true if validation should pass.
        """
        with open(COMPLIANCE_CASES, "r") as io:
            cases = yaml.load(io, Loader=yaml.loader.SafeLoader)

        for case in cases:
            with self.subTest(msg=case['description']):
                skip_reason = case.get("skip", None)
                if skip_reason is not None:
                    self.skipTest(skip_reason)

                dataset = case["dataset"]
                expected_valid = case.get("valid", False)
                
                if case.get("closed", True):
                    schema = self.kitchen_sink_json_schema
                else:
                    schema = self.kitchen_sink_json_schema_not_closed
                
                do_validate = lambda: jsonschema.validate(dataset, schema)
                if expected_valid:
                    # this will raise an exception and fail the test if the 
                    # instance does *not* validate
                    do_validate()
                else:
                    self.assertRaises(jsonschema.ValidationError, do_validate)

if __name__ == "__main__":
    unittest.main()
