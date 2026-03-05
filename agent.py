from tools import web_search
from logger import AuditLogger


class ResearchAgent:

    def __init__(self):

        self.logger = AuditLogger()


    def run(self, query):

        step = 1

        self.logger.log(step, "User Query", query, "Accepted")

        step += 1


        sub_question = "Explain " + query

        self.logger.log(step, "Query Decomposition", query, sub_question)

        step += 1


        result = web_search(sub_question)

        self.logger.log(step, "Tool Execution", sub_question, result)

        step += 1


        final_report = "Research Result:\n\n" + result

        self.logger.log(step, "Final Report Generated", result, final_report)

        logs = self.logger.save_logs()

        return final_report, logs