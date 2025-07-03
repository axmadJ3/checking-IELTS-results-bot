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
