from lxml import etree
from zeep import xsd

# Monkey patch relacionado a este PR: https://github.com/mvantellingen/python-zeep/pull/1384
#
# Foi necessário essa alteração devido ao fato da biblioteca "Zeep" não fornecer o tratamento
# para WSDLs que consistem em multiplos tipos complexos aninhados que esperam uma entrada do
# tipo "any", e a entrada fornecida é um objeto etree.
#
# O problema foi encontrado na implementação de DFe utilizando as bibliotecas nfelib e erpbrasil.edoc.
def custom_render(self, parent, value, render_path):
    if not isinstance(value, list):
        values = [value]
    else:
        values = value

    self.validate(values, render_path)

    child_path = render_path
    for value in xsd.utils.max_occurs_iter(self.max_occurs, values):
        for name, element in self.elements_nested:
            if name:
                if name in value:
                    element_value = value[name]
                    child_path += [name]
                elif isinstance(value, etree._Element):
                    element_value = value
                    child_path += [name]
                else:
                    element_value = xsd.const.NotSet
            else:
                element_value = value

            if element_value is xsd.const.SkipValue:
                continue

            if element_value is not None or not element.is_optional:
                element.render(parent, element_value, child_path)


def apply_zeep_monkey_patches():
    xsd.elements.indicators.OrderIndicator.render = custom_render
