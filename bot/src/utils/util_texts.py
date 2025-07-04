def build_prompt(topic, image, report):
    return f"""
    Проверь и оцени IELTS Writing Task 1.
    Тема: {topic}
    Изображение: {image}
    Отчёт:
    {report}

    Дай краткий комментарии по четырём критериям IELTS на английском:
    - Task Achievement
    - Coherence and Cohesion
    - Lexical Resource
    - Grammatical Range and Accuracy

    Также укажи примерные баллы и советы по улучшению.
    """


def start_text(name):
    return f'Hi {name}!, you can use this bot to find out your IELTS level!😊'


def about_text(name):
    return f"""
{name}, you can use this bot to find out your IELTS level!😊

Disclaimer⚠
This tool should be seen as a guide rather than a definitive score. Just like human reviewers, AI can be subjective, and the score provided may be accurate within 75%-95% when compared with an official IELTS score. 
Use this tool to complement your study, but not as a substitute for professional assessment or official IELTS grading.
"""
