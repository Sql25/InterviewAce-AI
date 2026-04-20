import streamlit as st

st.set_page_config(page_title="InterviewAce AI", page_icon="🤖")

st.title("🤖 InterviewAce AI")
st.subheader("SQL Interview Practice App")

# ============================
# MODE SELECTOR
# ============================
mode = st.radio("Choose Section", ["Section A (MCQ Test)", "Section B (Scenario Questions)"])

# ============================
# SECTION A — MCQ
# ============================
if mode == "Section A (MCQ Test)":

    st.header("📘 Section A - SQL MCQ Test (100 Marks)")

    questions = [
        {
            "q": "Find second highest salary?",
            "options": [
                "MAX(salary)",
                "MAX(salary) WHERE salary < MAX(salary)",
                "ORDER BY LIMIT 2",
                "MIN(salary)"
            ],
            "answer": 1,
            "hint": "Exclude highest first"
        },
        {
            "q": "INNER JOIN returns?",
            "options": [
                "All left rows",
                "All right rows",
                "Matching rows only",
                "NULL rows"
            ],
            "answer": 2,
            "hint": "Intersection"
        },
        {
            "q": "LEFT JOIN returns?",
            "options": [
                "Only matches",
                "All left + matched right",
                "Only right",
                "No NULLs"
            ],
            "answer": 1,
            "hint": "Left always preserved"
        },
        {
            "q": "HAVING is used for?",
            "options": [
                "Before grouping",
                "Filter aggregated data",
                "Sorting",
                "Joining"
            ],
            "answer": 1,
            "hint": "After GROUP BY"
        },
        {
            "q": "ROW_NUMBER() does?",
            "options": [
                "Counts rows",
                "Unique number per row",
                "Groups data",
                "Removes duplicates"
            ],
            "answer": 1,
            "hint": "Ranking without ties"
        },
        {
            "q": "RANK() does?",
            "options": [
                "No duplicates",
                "Same values same rank",
                "Sequential always",
                "Removes duplicates"
            ],
            "answer": 1,
            "hint": "Handles ties"
        },
        {
            "q": "UNION does?",
            "options": [
                "Keeps duplicates",
                "Same as UNION ALL",
                "Removes duplicates",
                "Slower than JOIN"
            ],
            "answer": 2,
            "hint": "Removes duplicates"
        },
        {
            "q": "CASE is used for?",
            "options": [
                "Loop",
                "Condition logic",
                "Join",
                "Sort"
            ],
            "answer": 1,
            "hint": "IF-ELSE"
        },
        {
            "q": "CTE is?",
            "options": [
                "Permanent table",
                "Temporary result set",
                "Index",
                "View"
            ],
            "answer": 1,
            "hint": "WITH clause"
        },
        {
            "q": "DELETE vs TRUNCATE?",
            "options": [
                "DELETE no rollback",
                "TRUNCATE has WHERE",
                "DELETE logs rows",
                "TRUNCATE slower"
            ],
            "answer": 2,
            "hint": "Logging"
        }
    ]

    if "answers" not in st.session_state:
        st.session_state.answers = [None] * len(questions)

    for i, q in enumerate(questions):
        st.subheader(f"Q{i+1}. {q['q']}")
        st.caption(f"💡 Hint: {q['hint']}")

        st.session_state.answers[i] = st.radio(
            "Choose answer:",
            q["options"],
            key=f"q{i}"
        )

    if st.button("Submit Test"):
        score = 0

        for i, q in enumerate(questions):
            if q["options"].index(st.session_state.answers[i]) == q["answer"]:
                score += 10

        st.success(f"🎯 Your Score: {score}/100")

        if score >= 90:
            st.success("🔥 Excellent!")
        elif score >= 70:
            st.info("👍 Strong")
        else:
            st.warning("📘 Needs Improvement")

        with st.expander("📊 Show Answers"):
            for i, q in enumerate(questions):
                st.write(f"Q{i+1}: {q['options'][q['answer']]}")

# ============================
# SECTION B — SCENARIO
# ============================
else:

    st.header("📊 Section B - Scenario Questions")

    questions = [
        "Design a database for credit card transactions.",
        "Write query for top 3 profitable regions.",
        "How to identify customer churn?",
        "How to optimize SQL queries?",
        "How to handle NULL values?"
    ]

    if "index" not in st.session_state:
        st.session_state.index = 0

    def evaluate(answer):
        score = 5
        strengths = []
        improvements = []

        ans = answer.lower()

        if "group by" in ans:
            score += 1
            strengths.append("Good use of aggregation")

        if "join" in ans:
            score += 1
            strengths.append("Understands joins")

        if "index" in ans:
            score += 1
            strengths.append("Performance awareness")

        if "result" in ans or "improve" in ans:
            score += 2
            strengths.append("Shows outcome thinking")

        if len(answer.split()) < 30:
            improvements.append("Add more explanation")

        if "example" not in ans:
            improvements.append("Include example")

        score = min(score, 10)

        return score, strengths, improvements

    if st.session_state.index < len(questions):

        q = questions[st.session_state.index]
        st.info(f"Question {st.session_state.index + 1}: {q}")

        ans = st.text_area("Your Answer:", height=150)

        if st.button("Submit Answer"):

            if ans.strip():
                score, strengths, improvements = evaluate(ans)

                st.success(f"Score: {score}/10")

                st.write("### Strengths")
                for s in strengths:
                    st.write(f"- {s}")

                st.write("### Improvements")
                for i in improvements:
                    st.write(f"- {i}")

                st.session_state.next = True
            else:
                st.warning("Enter answer first")

        if st.session_state.get("next"):
            if st.button("Next ➡️"):
                st.session_state.index += 1
                st.session_state.next = False
                st.rerun()

    else:
        st.success("🎉 Completed Section B")
        if st.button("Restart"):
            st.session_state.index = 0
            st.rerun()