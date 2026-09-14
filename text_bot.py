from main import find_intent


test_questions = [
    "What is GKS-U?",
    "Do I need IELTS for GKS?",
    "What documents are required for GKS?",
    "What is the UIC Track?",
    "What is the difference between Embassy Track and University Track?",
    "Can I apply without TOPIK?",
    "What is an academic transcript?",
    "What is a recommendation letter?",
    "How does the GKS interview work?",
    "What are the benefits of GKS?",
    "documnts for gks",
    "is ielts needed",
]


print("=" * 60)
print("             GKS APPLICANT ASSISTANT")
print("                  TEST SUITE")
print("=" * 60)

passed = 0

for question in test_questions:
    intent, confidence = find_intent(question)

    if intent is not None and confidence >= 0.70:
        print(f"\n✅ PASS: {question}")
        print(f"   Intent: {intent}")
        print(f"   Confidence: {confidence:.2f}")
        passed += 1
    else:
        print(f"\n❌ FAIL: {question}")
        print(f"   Intent: {intent}")
        print(f"   Confidence: {confidence:.2f}")


print("\n" + "=" * 60)
print(f"RESULT: {passed}/{len(test_questions)} tests passed")
print("=" * 60)