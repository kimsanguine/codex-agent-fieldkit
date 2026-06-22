import unittest

from faq_agent_lite import FAQAgent, load_faqs


class FAQAgentTest(unittest.TestCase):
    def setUp(self) -> None:
        self.agent = FAQAgent(load_faqs())

    def test_billing_question_routes_to_billing_faq(self) -> None:
        result = self.agent.answer("Can I change my billing date?")
        self.assertEqual("FAQ-001", result.source_id)
        self.assertIn("billing-date change", result.answer)

    def test_claim_question_routes_to_claims_faq(self) -> None:
        result = self.agent.answer("What documents are needed for a claim?")
        self.assertEqual("FAQ-002", result.source_id)
        self.assertIn("claim form", result.answer)

    def test_unknown_question_uses_fallback(self) -> None:
        result = self.agent.answer("What is the weather in Seoul today?")
        self.assertEqual("NO_MATCH", result.source_id)
        self.assertEqual(0.0, result.confidence)

    def test_low_overlap_private_account_question_uses_fallback(self) -> None:
        result = self.agent.answer("What is my real account balance?")
        self.assertEqual("NO_MATCH", result.source_id)

    def test_demo_questions_file_is_used(self) -> None:
        from faq_agent_lite.cli import load_demo_questions

        questions = load_demo_questions()
        self.assertGreaterEqual(len(questions), 5)
        self.assertIn("What is my real account balance?", questions)


if __name__ == "__main__":
    unittest.main()
