
# Class: anonymous_slot_expression




URI: [linkml:AnonymousSlotExpression](https://w3id.org/linkml/AnonymousSlotExpression)


[![img](images/AnonymousSlotExpression.svg)](images/AnonymousSlotExpression.svg)

## Parents

 *  is_a: [AnonymousExpression](AnonymousExpression.md) - An abstract parent class for any nested expression

## Uses Mixin

 *  mixin: [SlotExpression](SlotExpression.md) - an expression that constrains the range of values a slot can take

## Referenced by Class

 *  **None** *[all_members](all_members.md)*  <sub>0..1</sub>  **[AnonymousSlotExpression](AnonymousSlotExpression.md)**
 *  **None** *[has_member](has_member.md)*  <sub>0..1</sub>  **[AnonymousSlotExpression](AnonymousSlotExpression.md)**
 *  **[SlotExpression](SlotExpression.md)** *[slot_expression➞all_of](slot_expression_all_of.md)*  <sub>0..\*</sub>  **[AnonymousSlotExpression](AnonymousSlotExpression.md)**
 *  **[SlotExpression](SlotExpression.md)** *[slot_expression➞any_of](slot_expression_any_of.md)*  <sub>0..\*</sub>  **[AnonymousSlotExpression](AnonymousSlotExpression.md)**
 *  **[SlotExpression](SlotExpression.md)** *[slot_expression➞exactly_one_of](slot_expression_exactly_one_of.md)*  <sub>0..\*</sub>  **[AnonymousSlotExpression](AnonymousSlotExpression.md)**
 *  **[SlotExpression](SlotExpression.md)** *[slot_expression➞none_of](slot_expression_none_of.md)*  <sub>0..\*</sub>  **[AnonymousSlotExpression](AnonymousSlotExpression.md)**

## Attributes


### Mixed in from slot_expression:

 * [range](range.md)  <sub>0..1</sub>
     * Description: defines the type of the object of the slot.  Given the following slot definition
  S1:
    domain: C1
    range:  C2
the declaration
  X:
    S1: Y

implicitly asserts Y is an instance of C2

     * Range: [Element](Element.md)
     * in subsets: (SpecificationSubset,MinimalSubset,BasicSubset,RelationalModelProfile,ObjectOrientedProfile)

### Mixed in from slot_expression:

 * [range_expression](range_expression.md)  <sub>0..1</sub>
     * Description: A range that is described as a boolean expression combining existing ranges
     * Range: [AnonymousClassExpression](AnonymousClassExpression.md)
     * in subsets: (SpecificationSubset)

### Mixed in from slot_expression:

 * [enum_range](enum_range.md)  <sub>0..1</sub>
     * Description: An inlined enumeration
     * Range: [EnumExpression](EnumExpression.md)
     * in subsets: (SpecificationSubset)

### Mixed in from slot_expression:

 * [required](required.md)  <sub>0..1</sub>
     * Description: true means that the slot must be present in instances of the class definition
     * Range: [Boolean](types/Boolean.md)
     * in subsets: (SpecificationSubset,MinimalSubset,BasicSubset,RelationalModelProfile,ObjectOrientedProfile)

### Mixed in from slot_expression:

 * [recommended](recommended.md)  <sub>0..1</sub>
     * Description: true means that the slot should be present in instances of the class definition, but this is not required
     * Range: [Boolean](types/Boolean.md)
     * in subsets: (SpecificationSubset,BasicSubset)

### Mixed in from slot_expression:

 * [inlined](inlined.md)  <sub>0..1</sub>
     * Description: True means that keyed or identified slot appears in an outer structure by value.  False means that only the key or identifier for the slot appears within the domain, referencing a structure that appears elsewhere.
     * Range: [Boolean](types/Boolean.md)
     * in subsets: (SpecificationSubset,BasicSubset)

### Mixed in from slot_expression:

 * [inlined_as_list](inlined_as_list.md)  <sub>0..1</sub>
     * Description: True means that an inlined slot is represented as a list of range instances.  False means that an inlined slot is represented as a dictionary, whose key is the slot key or identifier and whose value is the range instance.
     * Range: [Boolean](types/Boolean.md)
     * in subsets: (SpecificationSubset,BasicSubset)

### Mixed in from slot_expression:

 * [minimum_value](minimum_value.md)  <sub>0..1</sub>
     * Description: For ordinal ranges, the value must be equal to or higher than this
     * Range: [Anything](Anything.md)
     * in subsets: (SpecificationSubset,BasicSubset)

### Mixed in from slot_expression:

 * [maximum_value](maximum_value.md)  <sub>0..1</sub>
     * Description: For ordinal ranges, the value must be equal to or lower than this
     * Range: [Anything](Anything.md)
     * in subsets: (SpecificationSubset,BasicSubset)

### Mixed in from slot_expression:

 * [pattern](pattern.md)  <sub>0..1</sub>
     * Description: the string value of the slot must conform to this regular expression expressed in the string
     * Range: [String](types/String.md)
     * in subsets: (SpecificationSubset,BasicSubset)

### Mixed in from slot_expression:

 * [structured_pattern](structured_pattern.md)  <sub>0..1</sub>
     * Description: the string value of the slot must conform to the regular expression in the pattern expression
     * Range: [PatternExpression](PatternExpression.md)
     * in subsets: (SpecificationSubset)

### Mixed in from slot_expression:

 * [unit](unit.md)  <sub>0..1</sub>
     * Description: an encoding of a unit
     * Range: [UnitOfMeasure](UnitOfMeasure.md)

### Mixed in from slot_expression:

 * [implicit_prefix](implicit_prefix.md)  <sub>0..1</sub>
     * Description: Causes the slot value to be interpreted as a uriorcurie after prefixing with this string
     * Range: [String](types/String.md)
     * in subsets: (SpecificationSubset)

### Mixed in from slot_expression:

 * [value_presence](value_presence.md)  <sub>0..1</sub>
     * Description: if true then a value must be present (for lists there must be at least one value). If false then a value must be absent (for lists, must be empty)
     * Range: [presence_enum](presence_enum.md)

### Mixed in from slot_expression:

 * [equals_string](equals_string.md)  <sub>0..1</sub>
     * Description: the slot must have range string and the value of the slot must equal the specified value
     * Range: [String](types/String.md)
     * in subsets: (SpecificationSubset)

### Mixed in from slot_expression:

 * [equals_string_in](equals_string_in.md)  <sub>0..\*</sub>
     * Description: the slot must have range string and the value of the slot must equal one of the specified values
     * Range: [String](types/String.md)
     * in subsets: (SpecificationSubset)

### Mixed in from slot_expression:

 * [equals_number](equals_number.md)  <sub>0..1</sub>
     * Description: the slot must have range of a number and the value of the slot must equal the specified value
     * Range: [Integer](types/Integer.md)

### Mixed in from slot_expression:

 * [equals_expression](equals_expression.md)  <sub>0..1</sub>
     * Description: the value of the slot must equal the value of the evaluated expression
     * Range: [String](types/String.md)
     * in subsets: (SpecificationSubset)

### Mixed in from slot_expression:

 * [exact_cardinality](exact_cardinality.md)  <sub>0..1</sub>
     * Description: the exact number of entries for a multivalued slot
     * Range: [Integer](types/Integer.md)
     * in subsets: (SpecificationSubset)

### Mixed in from slot_expression:

 * [minimum_cardinality](minimum_cardinality.md)  <sub>0..1</sub>
     * Description: the minimum number of entries for a multivalued slot
     * Range: [Integer](types/Integer.md)
     * in subsets: (SpecificationSubset)

### Mixed in from slot_expression:

 * [maximum_cardinality](maximum_cardinality.md)  <sub>0..1</sub>
     * Description: the maximum number of entries for a multivalued slot
     * Range: [Integer](types/Integer.md)
     * in subsets: (SpecificationSubset)

### Mixed in from slot_expression:

 * [has_member](has_member.md)  <sub>0..1</sub>
     * Description: the value of the slot is multivalued with at least one member satisfying the condition
     * Range: [AnonymousSlotExpression](AnonymousSlotExpression.md)
     * in subsets: (SpecificationSubset)

### Mixed in from slot_expression:

 * [all_members](all_members.md)  <sub>0..1</sub>
     * Description: the value of the slot is multivalued with all members satisfying the condition
     * Range: [AnonymousSlotExpression](AnonymousSlotExpression.md)
     * in subsets: (SpecificationSubset)

### Mixed in from slot_expression:

 * [slot_expression➞none_of](slot_expression_none_of.md)  <sub>0..\*</sub>
     * Description: holds if none of the expressions hold
     * Range: [AnonymousSlotExpression](AnonymousSlotExpression.md)
     * in subsets: (SpecificationSubset)

### Mixed in from slot_expression:

 * [slot_expression➞exactly_one_of](slot_expression_exactly_one_of.md)  <sub>0..\*</sub>
     * Description: holds if only one of the expressions hold
     * Range: [AnonymousSlotExpression](AnonymousSlotExpression.md)
     * in subsets: (SpecificationSubset)

### Mixed in from slot_expression:

 * [slot_expression➞any_of](slot_expression_any_of.md)  <sub>0..\*</sub>
     * Description: holds if at least one of the expressions hold
     * Range: [AnonymousSlotExpression](AnonymousSlotExpression.md)
     * in subsets: (SpecificationSubset)

### Mixed in from slot_expression:

 * [slot_expression➞all_of](slot_expression_all_of.md)  <sub>0..\*</sub>
     * Description: holds if all of the expressions hold
     * Range: [AnonymousSlotExpression](AnonymousSlotExpression.md)
     * in subsets: (SpecificationSubset)
