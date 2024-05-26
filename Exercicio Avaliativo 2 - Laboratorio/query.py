def obter_professor_por_nome(nome):
    query = "MATCH (t:Teacher {name: $nome}) RETURN t.ano_nasc AS ano_nasc, t.cpf AS cpf"
    return query, {"nome": nome}

def obter_professores_iniciando_com_letra(letra):
    query = "MATCH (t:Teacher) WHERE t.name STARTS WITH $letra RETURN t.name AS nome, t.cpf AS cpf"
    return query, {"letra": letra}

def obter_todas_as_cidades():
    query = "MATCH (c:City) RETURN c.name AS nome"
    return query, {}

def obter_escolas_no_intervalo(min_number, max_number):
    query = ("MATCH (s:School) WHERE s.number >= $min_number AND s.number <= $max_number "
             "RETURN s.name AS nome, s.address AS endereco, s.number AS numero")
    return query, {"min_number": min_number, "max_number": max_number}

def obter_professor_mais_velho_e_mais_novo():
    query = (
        "MATCH (t:Teacher) "
        "RETURN MIN(t.ano_nasc) AS mais_novo, MAX(t.ano_nasc) AS mais_velho"
    )
    return query, {}

def obter_media_populacional():
    query = (
        "MATCH (c:City) "
        "RETURN AVG(c.population) AS media_populacional"
    )
    return query, {}

def obter_cidade_por_cep(cep):
    query = (
        "MATCH (c:City {cep: $cep}) "
        "RETURN REPLACE(c.name, 'a', 'A') AS nome_modificado"
    )
    return query, {"cep": cep}

def obter_terceira_letra_dos_professores():
    query = (
        "MATCH (t:Teacher) "
        "RETURN SUBSTRING(t.name, 2, 1) AS terceira_letra"
    )
    return query, {}
