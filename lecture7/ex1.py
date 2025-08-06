survey_results = [
    ["Python", "JavaScript", "C++"],
    ["Python", "JavaScript", "C#"],
    ["Python", "Java"],
    ["Python", "C++" ,"JavaScript"],
    ["Python", "JavaScript", "C++", "Java"],
]


choice_sets = [set(i) for i in survey_results]
common_languages = set.intersection(*choice_sets)
print("Languages chosen by all participants:", common_languages)

only = set.union(*choice_sets) - choice_sets[0] - choice_sets[-1]
print("Languages only chosen by one participant:", only)

unique_languages = set.union(*choice_sets)
print("Number of unique languages:", len(unique_languages))

two = set.union(*choice_sets) - choice_sets[0] & choice_sets[-1]
print("Languages chosen by exactly two participants:", two)



