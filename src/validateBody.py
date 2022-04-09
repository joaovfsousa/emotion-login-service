class Validator():

  def isBodyValid(body, requiredFields): 
    def isNone(value):
      return value == None

    def bodyContains(value):
      return value in body

    areFieldValuesNone = map(isNone, body.items())
    containsRequiredField = map(contains, requiredFields)

    areValuesValid = not any(areFieldValuesNone)
    areFieldsValid = all(containsRequiredField)

    return areFieldsValid and areValuesValid
