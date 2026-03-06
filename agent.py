from tools import web_search
from logger import AuditLogger

class PlannerAgent:
    def plan(self, query):
        sub_questions = [
            f"What is {query}?",
            f"How does {query} work?",
            f"Examples of {query}"
        ]
        return sub_questions


class ResearchAgent:
    def research(self, question):
        result = web_search(question)
        return result


class VerificationAgent:
    def verify(self, results):
        score = min(100, len(results) * 30)
        return score


class ResearchSystem:

    def __init__(self):
        self.logger = AuditLogger()
        self.planner = PlannerAgent()
        self.researcher = ResearchAgent()
        self.verifier = VerificationAgent()

    def run(self, query):

        step = 1

        self.logger.log(step, "User Query", query, "Accepted")
        step += 1

        sub_questions = self.planner.plan(query)

        self.logger.log(step, "Planner Agent", query, sub_questions)
        step += 1

        results = []

        for q in sub_questions:
            res = self.researcher.research(q)
            results.append(res)

            self.logger.log(step, "Research Agent", q, res)
            step += 1

        confidence = self.verifier.verify(results)

        self.logger.log(step, "Verification Agent", results, f"Confidence {confidence}%")
        step += 1

        formatted_results = []

        for i, res in enumerate(results):
            if i == 0:
                formatted_results.append("### Definition\n" + res)
            elif i == 1:
                formatted_results.append("### How it Works\n" + res)
            elif i == 2:
                formatted_results.append("### Examples\n" + res)

        final_report = "\n\n".join(formatted_results)

        self.logger.log(step, "Final Report Generated", results, final_report)

        logs = self.logger.save_logs()

        return final_report, logs, confidence