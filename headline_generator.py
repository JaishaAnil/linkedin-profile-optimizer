def generate_headline(skills):
    skills_list = skills.split(",")

    formatted_skills = " | ".join(
        skill.strip() for skill in skills_list
    )

    return f"Aspiring Data Analyst | {formatted_skills}"