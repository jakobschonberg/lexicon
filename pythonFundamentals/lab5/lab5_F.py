#F1
def create_report(title, *sections, **metadata):
    d = dict(metadata)
    d["sections"] = sections
    d["title"] = title
    return d

#F2 and F3
report = create_report("TPS", "meetings", "coffee breaks", "report filling", "actual work",
                       time_waste = 15, work_time = 25, author = "John Doe", version = "1.0",
                       confidential = False, date = "2026-09-15")    

#F4
def summarize_report(report):
    print("Title:", report["title"])
    s = ""
    for section in report["sections"]:
        if s:
            s = s + ", "
        s = s + str(section)
    if s:
        print("Sections:", s)
    for key, value in report.items():
        if key != "title" and key != "sections":
            print(f"{key}: {value}")
    if not "author" in report.keys(): #F7
        print("author: ", "(unknown)") #F7

summarize_report(report)

#F5
def count_words(*sections):
    cnt = 0
    for section in sections:
        words = section.split()
        cnt += len(words)
    return cnt

print(count_words("Anchor", "Board Cable"))
print(count_words(*report["sections"]))

#F6
metadata0 = {"time_waste": 15, "work_time": 25, "author": "John Doe",
             "version": "1.0", "confidential": False, "date": "2026-09-15"}
metadata1 = {"version": "0.07", "confidential": True}
report0 = create_report("TPS", "meetings", "coffee breaks", "report filling",
                       "actual work", **metadata0)
report1 = create_report("TOP SECRET", **metadata1)
summarize_report(report0)
summarize_report(report1)

#F7
#Already ignoring all fields not supplied except for author which is handled if missing


                       