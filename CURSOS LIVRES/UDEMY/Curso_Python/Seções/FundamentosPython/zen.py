from colorama import Fore, Style, init

init()

def imprimir_zen():
    zen_ingles = [
        "The Zen of Python, by Tim Peters",
        "",
        "Beautiful is better than ugly.",
        "Explicit is better than implicit.",
        "Simple is better than complex.",
        "Complex is better than complicated.",
        "Flat is better than nested.",
        "Sparse is better than dense.",
        "Readability counts.",
        "Special cases aren't special enough to break the rules.",
        "Although practicality beats purity.",
        "Errors should never pass silently.",
        "Unless explicitly silenced.",
        "In the face of ambiguity, refuse the temptation to guess.",
        "There should be one-- and preferably only one --obvious way to do it.",
        "Although that way may not be obvious at first unless you're Dutch.",
        "Now is better than never.",
        "Although never is often better than *right* now.",
        "If the implementation is hard to explain, it's a bad idea.",
        "If the implementation is easy to explain, it may be a good idea.",
        "Namespaces are one honking great idea -- let's do more of those!",
    ]

    zen_portugues = [
        "O Zen do Python, por Tim Peters",
        "",
        "Bonito é melhor que feio.",
        "Explícito é melhor que implícito.",
        "Simples é melhor que complexo.",
        "Complexo é melhor que complicado.",
        "Plano é melhor que aninhado.",
        "Esparso é melhor que denso.",
        "Legibilidade conta.",
        "Casos especiais não são tão especiais a ponto de quebrar as regras.",
        "Embora a praticidade vença a pureza.",
        "Erros nunca devem passar silenciosamente.",
        "A menos que sejam explicitamente silenciados.",
        "Diante da ambiguidade, recuse a tentação de adivinhar.",
        "Deveria haver uma — e preferencialmente apenas uma — maneira óbvia de fazer algo.",
        "Embora essa maneira possa não ser óbvia de início, a menos que você seja holandês.",
        "Agora é melhor que nunca.",
        "Embora nunca seja frequentemente melhor que *agora mesmo*.",
        "Se a implementação é difícil de explicar, é uma má ideia.",
        "Se a implementação é fácil de explicar, pode ser uma boa ideia.",
        "Namespaces são uma ideia incrível — vamos fazer mais dessas!",
    ]

    explicacoes = [
        "O Zen do Python é uma coleção de princípios que guiam o design da linguagem Python.",
        "",
        "Código bonito e organizado é preferível a código confuso e desorganizado.",
        "É melhor ser claro e direto do que depender de comportamentos ocultos ou implícitos.",
        "Soluções simples são preferíveis a soluções complexas.",
        "Se a complexidade for necessária, é melhor que seja organizada e não confusa.",
        "Estruturas planas são mais fáceis de entender do que estruturas profundamente aninhadas.",
        "Código espaçado e bem organizado é melhor do que código denso e difícil de ler.",
        "A legibilidade do código é extremamente importante.",
        "Casos especiais não devem justificar a quebra de boas práticas ou regras gerais.",
        "A praticidade é mais importante do que a perfeição teórica.",
        "Erros devem ser tratados e nunca ignorados silenciosamente.",
        "A menos que você tenha um bom motivo para ignorar um erro.",
        "Em situações ambíguas, evite suposições e busque clareza.",
        "Deve haver uma maneira clara e óbvia de realizar uma tarefa.",
        "Essa maneira pode não ser óbvia no início, mas deve existir.",
        "Fazer algo agora é melhor do que adiar indefinidamente.",
        "Mas, às vezes, é melhor esperar do que fazer algo precipitado.",
        "Se o código é difícil de explicar, provavelmente não é uma boa solução.",
        "Se o código é fácil de explicar, é um sinal de que está bem projetado.",
        "Namespaces ajudam a organizar o código e evitar conflitos de nomes.",
    ]


    for ingles, portugues, explicacao in zip(zen_ingles, zen_portugues, explicacoes):
        print(Fore.RED + ingles) 
        print(Fore.CYAN + portugues) 
        print(Fore.YELLOW + f"Explicação: {explicacao}")  
        print(Style.RESET_ALL) 
        print() 

if __name__ == "__main__":
    imprimir_zen()