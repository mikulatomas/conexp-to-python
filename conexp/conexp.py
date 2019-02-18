import xmltodict


def cex_to_list(filename):
    with open(filename) as cex_file:
        content = xmltodict.parse(cex_file.read())

        cex_conceptual_system = content['ConceptualSystem']

        if cex_conceptual_system.get('Contexts'):
            cex_context = cex_conceptual_system['Contexts']['Context']

            context = extract_context(cex_context)

            if cex_conceptual_system.get('Lattices'):
                cex_lattice = cex_conceptual_system['Lattices']['Lattice']
                cex_concepts = cex_lattice['LineDiagram']['ConceptFigures']['LineDiagramFigure']

                concepts = extract_concepts(
                    cex_concepts, len(context['attributes']))

        return {
            'context': context,
            'concepts': concepts
        }


def extract_concepts(cex_concepts, n_of_attributes):
    concepts = []

    for concept in cex_concepts:
        intent = [False] * n_of_attributes

        if concept['Intent']:
            attrs = concept['Intent']['HasAttribute']

            if type(attrs) is list:
                for attr in attrs:
                    intent[int(attr['@AttributeIdentifier'])] = True
            else:
                intent[int(attrs['@AttributeIdentifier'])] = True

        concepts.append(intent)

    return concepts


def extract_context(cex_context):
    cex_attributes = cex_context['Attributes']['Attribute']
    cex_objects = cex_context['Objects']['Object']

    attributes = [attr['Name'] for attr in cex_attributes]
    objects = []
    table = []

    for obj in cex_objects:
        objects.append(obj['Name'])

        row = [False] * len(attributes)

        for intents in obj['Intent'].values():
            if type(intents) is list:
                for intent in intents:
                    row[int(intent['@AttributeIdentifier'])] = True
            else:
                row[int(intents['@AttributeIdentifier'])] = True

        table.append(row)

    return {
        'objects': objects,
        'attributes': attributes,
        'table': table
    }


# print(cex_to_list('sample2.cex'))
