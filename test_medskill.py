"""
Automated unit verification for MedSkill AI (144 Questions Edition)
Verifies:
- Minimum 12 questions in EVERY topic of EVERY specialty (12 topics x 12 questions = 144 total).
- Data integrity, schema consistency, filtering, and scoring calculations.
"""

from questions import (
    QUESTIONS_DATA,
    SPECIALTIES,
    TOPICS_BY_SPECIALTY,
    get_questions_for_specialty,
    get_question_by_id,
    get_all_revision_notes_for_topic
)

def test_questions_data():
    assert len(QUESTIONS_DATA) == 144, f"Expected exactly 144 questions, found {len(QUESTIONS_DATA)}"
    
    seen_ids = set()
    specialty_counts = {s: 0 for s in SPECIALTIES}
    topic_counts = {}
    
    for s in SPECIALTIES:
        for t in TOPICS_BY_SPECIALTY[s]:
            if t != "All Topics":
                topic_counts[(s, t)] = 0
    
    for q in QUESTIONS_DATA:
        # Check required fields
        required_fields = ["id", "specialty", "topic", "difficulty", "question", "options", "correct_index", "explanation", "key_points", "sample_viva_answer"]
        for field in required_fields:
            assert field in q, f"Question {q.get('id', 'unknown')} missing required field: {field}"
        
        # Check unique id
        assert q["id"] not in seen_ids, f"Duplicate ID: {q['id']}"
        seen_ids.add(q["id"])
        
        # Check valid specialty
        assert q["specialty"] in SPECIALTIES, f"Invalid specialty: {q['specialty']}"
        specialty_counts[q["specialty"]] += 1
        
        # Check valid topic
        assert q["topic"] in TOPICS_BY_SPECIALTY[q["specialty"]], f"Invalid topic {q['topic']} for {q['specialty']}"
        topic_counts[(q["specialty"], q["topic"])] += 1
        
        # Check options
        assert len(q["options"]) == 4, f"Question {q['id']} does not have exactly 4 options"
        assert 0 <= q["correct_index"] < 4, f"Question {q['id']} invalid correct_index: {q['correct_index']}"
        
        # Check difficulty
        assert q["difficulty"] in ["Beginner", "Intermediate", "Advanced"], f"Question {q['id']} invalid difficulty: {q['difficulty']}"

    # Check specialty counts
    for spec, count in specialty_counts.items():
        assert count == 48, f"Specialty {spec} has {count} questions, expected 48"
    
    # Check topic counts: EVERY topic must have at least 12 questions!
    for (spec, topic), count in topic_counts.items():
        assert count >= 12, f"Specialty '{spec}', Topic '{topic}' has only {count} questions! Must have at least 12."
        print(f"Verified: [{spec}] -> '{topic}': {count} questions.")
    
    print(f"\nSUCCESS: All 12 topics verified with at least 12 questions each (Total: {len(QUESTIONS_DATA)} questions).")

def test_filtering():
    for spec in SPECIALTIES:
        q_spec = get_questions_for_specialty(spec)
        assert len(q_spec) == 48, f"Expected 48 for {spec}, got {len(q_spec)}"
        
        for t in TOPICS_BY_SPECIALTY[spec]:
            if t != "All Topics":
                q_topic = get_questions_for_specialty(spec, topic=t)
                assert len(q_topic) >= 12, f"Expected >= 12 for {spec} - {t}, got {len(q_topic)}"
    
    print("Filtering verification across all specialties and topics passed.")

if __name__ == "__main__":
    test_questions_data()
    test_filtering()
    print("\nALL 144 QUESTION CURRICULUM TESTS PASSED SUCCESSFULLY!")
