"""
Builder script to generate the complete 144-question curriculum bank for MedSkill AI.
Contains exactly 12 high-yield, reviewed questions for each of the 12 curriculum topics:
- Respiratory Therapy (4 topics x 12 = 48 questions)
- Anaesthesia Technology (4 topics x 12 = 48 questions)
- Dialysis Technology (4 topics x 12 = 48 questions)
Total: 144 verified viva questions.
"""

import json

# Respiratory Therapy Questions (48 questions)
RT_AP_QUESTIONS = [
    {
        "id": "RT-AP-01",
        "specialty": "Respiratory Therapy",
        "topic": "Respiratory anatomy and physiology",
        "difficulty": "Beginner",
        "question": "What is the normal ratio of physiological dead space to tidal volume (Vd/Vt) in a healthy awake adult breathing room air?",
        "options": ["0.05 to 0.10", "0.20 to 0.35", "0.50 to 0.65", "0.70 to 0.85"],
        "correct_index": 1,
        "explanation": "In healthy conscious adults, normal dead space fraction (Vd/Vt) is approximately 0.20 to 0.35 (20-35%). In mechanically ventilated patients or those with severe V/Q mismatch and pulmonary embolism, Vd/Vt can exceed 0.50.",
        "key_points": [
            "Anatomical dead space is approximately 2 mL/kg of ideal body weight (~150 mL).",
            "Physiological dead space combines anatomical and alveolar dead space via the Enghoff-modified Bohr equation.",
            "Ventilator circuits and HME filters add mechanical dead space."
        ],
        "sample_viva_answer": "In healthy adults, the normal physiological dead space fraction is 0.20 to 0.35 (20% to 35% of tidal volume). It is calculated using the Enghoff-modified Bohr equation comparing PaCO2 with mixed expired PECO2."
    },
    {
        "id": "RT-AP-02",
        "specialty": "Respiratory Therapy",
        "topic": "Respiratory anatomy and physiology",
        "difficulty": "Intermediate",
        "question": "According to the oxyhemoglobin dissociation curve, which physiological change causes a 'right shift', promoting oxygen unloading at tissue capillaries?",
        "options": ["Decreased 2,3-BPG concentration", "Decreased core temperature (hypothermia)", "Increased hydrogen ion concentration (acidosis / lower pH)", "Decreased PaCO2 (hypocapnia)"],
        "correct_index": 2,
        "explanation": "A right shift in the oxyhemoglobin curve indicates decreased affinity of hemoglobin for oxygen, promoting oxygen delivery to tissues. Factors causing a right shift include increased H+ (acidosis / lower pH), increased PaCO2, elevated temperature, and increased 2,3-BPG (Bohr effect).",
        "key_points": [
            "Right shift causes: Acidosis, Hypercapnia, Hyperthermia, Increased 2,3-DPG (Mnemonic: CADET face Right).",
            "P50 increases from normal baseline of ~26.8 mmHg.",
            "Left shift causes: Alkalosis, Hypothermia, Hypocapnia, Carboxyhemoglobin."
        ],
        "sample_viva_answer": "A rightward shift is caused by acidosis, increased PaCO2, hyperthermia, and increased 2,3-BPG. This decreases hemoglobin affinity for oxygen and facilitates unloading to metabolically active peripheral tissues."
    },
    {
        "id": "RT-AP-03",
        "specialty": "Respiratory Therapy",
        "topic": "Respiratory anatomy and physiology",
        "difficulty": "Advanced",
        "question": "Using the alveolar gas equation at sea level (barometric pressure 760 mmHg, water vapor pressure 47 mmHg, respiratory quotient 0.8), what is the normal ideal alveolar oxygen tension (PAO2) on room air (FiO2 0.21) with a PaCO2 of 40 mmHg?",
        "options": ["75 mmHg", "100 mmHg", "125 mmHg", "150 mmHg"],
        "correct_index": 1,
        "explanation": "PAO2 = [FiO2 * (PB - PH2O)] - (PaCO2 / R) = [0.21 * (760 - 47)] - (40 / 0.8) = [0.21 * 713] - 50 = 149.7 - 50 = ~100 mmHg.",
        "key_points": [
            "Normal room air PAO2 is approximately 100 mmHg at sea level.",
            "Normal arterial-alveolar (A-a) gradient on room air is 5-15 mmHg in young adults.",
            "Elevated A-a gradient indicates parenchymal lung disease, V/Q mismatch, or shunt."
        ],
        "sample_viva_answer": "Ideal alveolar oxygen tension (PAO2) is calculated using the alveolar gas equation and equals approximately 100 mmHg on room air at sea level when PaCO2 is 40 mmHg."
    },
    {
        "id": "RT-AP-04",
        "specialty": "Respiratory Therapy",
        "topic": "Respiratory anatomy and physiology",
        "difficulty": "Beginner",
        "question": "What two lung volumes combine to make up the Functional Residual Capacity (FRC)?",
        "options": ["Tidal Volume + Inspiratory Reserve Volume", "Expiratory Reserve Volume + Residual Volume", "Inspiratory Capacity + Vital Capacity", "Residual Volume + Tidal Volume"],
        "correct_index": 1,
        "explanation": "Functional Residual Capacity (FRC) is the volume of gas remaining in the lungs at the end of a normal passive tidal expiration. It equals the sum of Expiratory Reserve Volume (ERV) and Residual Volume (RV).",
        "key_points": [
            "FRC = ERV + RV (~2400 mL in a 70 kg adult).",
            "FRC serves as an oxygen reservoir preventing arterial hypoxemia between breaths.",
            "FRC decreases in supine position, obesity, pregnancy, and general anaesthesia."
        ],
        "sample_viva_answer": "FRC consists of the Expiratory Reserve Volume plus the Residual Volume. It represents the resting equilibrium volume where the inward recoil of the lungs balances the outward recoil of the chest wall."
    },
    {
        "id": "RT-AP-05",
        "specialty": "Respiratory Therapy",
        "topic": "Respiratory anatomy and physiology",
        "difficulty": "Intermediate",
        "question": "In West Zone 1 of the lung in an upright human, what is the relationship between alveolar pressure (PA), arterial pressure (Pa), and venous pressure (Pv)?",
        "options": ["Pa > Pv > PA", "Pa > PA > Pv", "PA > Pa > Pv", "Pv > PA > Pa"],
        "correct_index": 2,
        "explanation": "In West Zone 1 (alveolar dead space), alveolar pressure exceeds pulmonary arterial pressure (PA > Pa > Pv), causing capillaries to be compressed shut and resulting in ventilation without perfusion.",
        "key_points": [
            "Zone 1: PA > Pa > Pv (ventilated but unperfused - dead space).",
            "Zone 2: Pa > PA > Pv (waterfall effect; flow determined by Pa - PA).",
            "Zone 3: Pa > Pv > PA (continuous blood flow; dependent lung bases)."
        ],
        "sample_viva_answer": "In West Zone 1, alveolar pressure exceeds pulmonary arterial and venous pressures (PA > Pa > Pv), leading to capillary collapse and physiological dead space ventilation."
    },
    {
        "id": "RT-AP-06",
        "specialty": "Respiratory Therapy",
        "topic": "Respiratory anatomy and physiology",
        "difficulty": "Advanced",
        "question": "What is the physiological mechanism of Hypoxic Pulmonary Vasoconstriction (HPV)?",
        "options": ["Systemic hypotension causing generalized capillary collapse", "Localized pre-capillary arteriolar constriction in poorly ventilated, hypoxic alveoli to redirect blood to well-ventilated regions", "Sympathetic discharge dilating pulmonary venous beds", "Nitric oxide overproduction in atelectatic segments"],
        "correct_index": 1,
        "explanation": "HPV is an intrinsic, protective pulmonary reflex where low alveolar PO2 (< 60 mmHg) triggers contraction of pulmonary vascular smooth muscle in under-ventilated segments, redirecting blood flow to better-oxygenated lung zones to preserve V/Q matching.",
        "key_points": [
            "Triggered primarily by alveolar hypoxia, not mixed venous hypoxia.",
            "Blunted by volatile anaesthetic agents, vasodilators, and severe alkalosis.",
            "Generalized HPV at high altitude can trigger High Altitude Pulmonary Edema (HAPE)."
        ],
        "sample_viva_answer": "Hypoxic Pulmonary Vasoconstriction is an auto-regulatory mechanism that constricts arterioles supplying poorly ventilated, hypoxic alveoli, diverting pulmonary blood flow toward well-ventilated areas to optimize ventilation-perfusion matching."
    },
    {
        "id": "RT-AP-07",
        "specialty": "Respiratory Therapy",
        "topic": "Respiratory anatomy and physiology",
        "difficulty": "Intermediate",
        "question": "How is the major proportion (approximately 70%) of carbon dioxide transported in human blood?",
        "options": ["Physically dissolved in plasma", "Chemically bound to hemoglobin amino groups as carbamino compounds", "As bicarbonate ions (HCO3-) in plasma generated via carbonic anhydrase in erythrocytes", "In gaseous bubbles bound to plasma albumin"],
        "correct_index": 2,
        "explanation": "About 70% of CO2 is carried as bicarbonate (HCO3-). Inside erythrocytes, CO2 combines with water via carbonic anhydrase to form carbonic acid, which dissociates into H+ and HCO3-. The bicarbonate exits into plasma in exchange for chloride (chloride shift / Hamburger phenomenon).",
        "key_points": [
            "70% as plasma bicarbonate (HCO3-).",
            "20-23% bound to hemoglobin as carbamino-hemoglobin.",
            "7-10% physically dissolved in plasma (PCO2 * 0.03 mL/dL/mmHg)."
        ],
        "sample_viva_answer": "Approximately 70% of carbon dioxide is transported in blood as plasma bicarbonate ions generated inside red blood cells through the action of carbonic anhydrase and maintained by the chloride shift."
    },
    {
        "id": "RT-AP-08",
        "specialty": "Respiratory Therapy",
        "topic": "Respiratory anatomy and physiology",
        "difficulty": "Beginner",
        "question": "What is the primary muscle of inspiration responsible for approximately 75% of normal quiet breathing tidal volume?",
        "options": ["Internal intercostal muscles", "Diaphragm", "Sternocleidomastoid", "Rectus abdominis"],
        "correct_index": 1,
        "explanation": "The diaphragm is the primary inspiratory muscle. Innervated by the phrenic nerves (C3, C4, C5), its contraction increases the vertical and transverse dimensions of the thoracic cavity, generating negative intrapleural pressure that draws air in.",
        "key_points": [
            "Normal excursion is 1-2 cm during quiet breathing, up to 10 cm during forced inspiration.",
            "Quiet expiration is purely passive due to lung elastic recoil.",
            "Accessory muscles (sternocleidomastoid, scalenes) recruit during respiratory distress."
        ],
        "sample_viva_answer": "The diaphragm is the primary muscle of quiet inspiration, accounting for 70-75% of resting tidal volume. It is innervated by the phrenic nerves originating from cervical roots C3 to C5."
    },
    {
        "id": "RT-AP-09",
        "specialty": "Respiratory Therapy",
        "topic": "Respiratory anatomy and physiology",
        "difficulty": "Advanced",
        "question": "Which equation correctly calculates the total oxygen content of arterial blood (CaO2)?",
        "options": ["CaO2 = (1.34 * Hb * SaO2) + (0.003 * PaO2)", "CaO2 = (0.003 * Hb * SaO2) + (1.34 * PaO2)", "CaO2 = (Hb * PaO2) / 100", "CaO2 = (SaO2 / Hb) + (0.03 * PaCO2)"],
        "correct_index": 0,
        "explanation": "CaO2 = (1.34 mL O2/g Hb * Hb in g/dL * SaO2) + (0.003 mL/dL/mmHg * PaO2). In a normal individual with Hb 15 g/dL, SaO2 98%, and PaO2 100 mmHg, CaO2 is approximately 20 mL O2 per 100 mL of blood.",
        "key_points": [
            "1.34 is Hufner's constant for binding capacity of 1 g of hemoglobin.",
            "Dissolved oxygen contributes only ~0.3 mL/dL at PaO2 of 100 mmHg.",
            "Hemoglobin concentration is the overwhelmingly dominant factor in arterial oxygen content."
        ],
        "sample_viva_answer": "Arterial oxygen content equals (1.34 times hemoglobin concentration times arterial oxygen saturation) plus dissolved oxygen (0.003 times PaO2), yielding approximately 20 mL of oxygen per 100 mL of blood."
    },
    {
        "id": "RT-AP-10",
        "specialty": "Respiratory Therapy",
        "topic": "Respiratory anatomy and physiology",
        "difficulty": "Intermediate",
        "question": "What is the classic diagnostic feature that distinguishes an intrapulmonary anatomical or physiological shunt (V/Q = 0) from simple V/Q mismatch on arterial blood gases?",
        "options": ["Shunt responds rapidly with high PaO2 when 100% oxygen is administered", "True shunt shows minimal or refractory improvement in PaO2 despite 100% supplemental FiO2", "Shunt always produces severe hypercapnia", "Shunt immediately normalizes dead space fraction"],
        "correct_index": 1,
        "explanation": "Because shunted blood bypasses ventilated alveoli completely, administering 100% FiO2 cannot oxygenate blood flowing through the shunt. Refractory hypoxemia on 100% FiO2 is the hallmark of a significant true shunt (e.g., dense ARDS, consolidated pneumonia, atelectasis).",
        "key_points": [
            "V/Q mismatch corrects significantly with supplemental FiO2.",
            "True shunt (V/Q = 0) is refractory to oxygen therapy and requires PEEP/recruitment.",
            "Normal anatomical shunt is 2-5% of cardiac output (bronchial and thebesian veins)."
        ],
        "sample_viva_answer": "A true intrapulmonary shunt is refractory to supplemental oxygen therapy, meaning PaO2 fails to rise significantly even on 100% FiO2, because shunted venous blood bypasses ventilated lung units entirely."
    },
    {
        "id": "RT-AP-11",
        "specialty": "Respiratory Therapy",
        "topic": "Respiratory anatomy and physiology",
        "difficulty": "Beginner",
        "question": "What is the primary role of pulmonary surfactant synthesized by type II alveolar epithelial cells?",
        "options": ["To increase alveolar surface tension and promote lung collapse", "To reduce alveolar surface tension, preventing alveolar collapse at low lung volumes and stabilizing alveoli of varying sizes", "To hydrolyze inhaled pathogens directly", "To speed up oxygen diffusion through the capillary endothelium"],
        "correct_index": 1,
        "explanation": "According to the Law of Laplace (P = 2T / r), smaller alveoli would empty into larger alveoli without surfactant. Surfactant (primarily dipalmitoylphosphatidylcholine / DPPC) reduces surface tension proportionally more in smaller alveoli, stabilizing them and reducing the work of breathing.",
        "key_points": [
            "Synthesized and secreted by Type II pneumocytes.",
            "Prevents end-expiratory atelectasis and increases lung compliance.",
            "Deficiency in preterm neonates causes Infant Respiratory Distress Syndrome (IRDS)."
        ],
        "sample_viva_answer": "Pulmonary surfactant reduces surface tension at the air-liquid interface of alveoli, preventing alveolar collapse during expiration, equalizing pressure across alveoli of different sizes, and markedly reducing the muscular work of breathing."
    },
    {
        "id": "RT-AP-12",
        "specialty": "Respiratory Therapy",
        "topic": "Respiratory anatomy and physiology",
        "difficulty": "Advanced",
        "question": "Which method is considered the clinical gold standard for measuring anatomical dead space at the bedside?",
        "options": ["Enghoff modification of Bohr equation", "Fowler's single-breath nitrogen washout method", "Carbon dioxide rebreathing loop", "Helium dilution lung volume test"],
        "correct_index": 1,
        "explanation": "Fowler's method measures anatomical dead space by having the patient take a single vital capacity breath of 100% oxygen and analyzing the exhaled nitrogen concentration. Phase I is pure dead space (0% N2), and an equal-area vertical boundary line defines anatomical dead space.",
        "key_points": [
            "Fowler's method measures anatomical dead space.",
            "Bohr equation measures physiological dead space.",
            "Difference between physiological and anatomical dead space is alveolar dead space."
        ],
        "sample_viva_answer": "Fowler's single-breath nitrogen washout method is the standard physiological technique for measuring anatomical dead space, utilizing 100% oxygen inhalation and continuous analysis of expired nitrogen."
    }
]

RT_OT_QUESTIONS = [
    {
        "id": "RT-OT-01",
        "specialty": "Respiratory Therapy",
        "topic": "Oxygen therapy",
        "difficulty": "Beginner",
        "question": "What is the approximate FiO2 delivered by a simple face mask at an oxygen flow rate of 6 to 10 L/min?",
        "options": ["21% to 30%", "35% to 55%", "70% to 90%", "95% to 100%"],
        "correct_index": 1,
        "explanation": "A simple face mask delivers an FiO2 of approximately 35% to 55% at oxygen flow rates of 6-10 L/min. A minimum flow of 5-6 L/min is mandatory to flush exhaled CO2 from the mask reservoir and avoid carbon dioxide rebreathing.",
        "key_points": [
            "Flow rate must be at least 5-6 L/min to prevent CO2 rebreathing.",
            "FiO2 varies with the patient's inspiratory peak flow and mask fit.",
            "Classified as a variable-performance (low-flow) oxygen delivery system."
        ],
        "sample_viva_answer": "A simple face mask delivers an FiO2 between 35% and 55% at 6 to 10 L/min. The flow rate must never be kept below 5 L/min to prevent carbon dioxide rebreathing inside the mask reservoir."
    },
    {
        "id": "RT-OT-02",
        "specialty": "Respiratory Therapy",
        "topic": "Oxygen therapy",
        "difficulty": "Intermediate",
        "question": "Which oxygen delivery device relies on the Bernoulli principle and air entrainment to deliver a fixed, precise FiO2 regardless of the patient's breathing pattern?",
        "options": ["Nasal cannula", "Non-rebreather mask (NRB)", "Venturi (Air-entrainment) mask", "Simple face mask"],
        "correct_index": 2,
        "explanation": "The Venturi mask (air-entrainment mask) operates on Bernoulli's principle and the jet mixing effect. High-velocity oxygen enters through an orifice, creating a negative pressure that entrains room air through calibrated ports, delivering a fixed and accurate FiO2.",
        "key_points": [
            "Fixed-performance (high-flow) delivery system.",
            "Crucial for patients with chronic hypercapnic respiratory failure (e.g., severe COPD).",
            "Color-coded jet adapters or adjustable barrels correspond to specific FiO2 settings (24% to 50%)."
        ],
        "sample_viva_answer": "The Venturi mask utilizes Bernoulli's principle and air entrainment to provide a precise, fixed FiO2 independent of the patient's respiratory rate or tidal volume, making it the device of choice in COPD patients vulnerable to hypercapnia."
    },
    {
        "id": "RT-OT-03",
        "specialty": "Respiratory Therapy",
        "topic": "Oxygen therapy",
        "difficulty": "Beginner",
        "question": "Using the standard clinical 'Rule of 4' for a standard nasal cannula, what is the estimated FiO2 delivered to an adult patient at an oxygen flow rate of 3 L/min?",
        "options": ["24%", "28%", "32%", "40%"],
        "correct_index": 2,
        "explanation": "On room air, baseline FiO2 is 21%. Each 1 L/min of oxygen flow adds approximately 4% FiO2. At 1 L/min: ~24%; at 2 L/min: ~28%; at 3 L/min: ~32%; at 4 L/min: ~36%.",
        "key_points": [
            "Rule of 4: FiO2 = 20% + (4 * Flow in L/min).",
            "Flow rates above 4-6 L/min cause severe nasal mucosal drying and discomfort.",
            "Actual FiO2 varies with mouth vs. nose breathing and peak inspiratory demand."
        ],
        "sample_viva_answer": "By the Rule of 4, each liter of nasal cannula flow adds approximately 4% FiO2 to the 21% baseline. At 3 L/min, the estimated delivered FiO2 is approximately 32%."
    },
    {
        "id": "RT-OT-04",
        "specialty": "Respiratory Therapy",
        "topic": "Oxygen therapy",
        "difficulty": "Intermediate",
        "question": "What is the purpose of the one-way valves located on the exhalation ports and between the reservoir bag and face mask on a Non-Rebreather Mask (NRB)?",
        "options": ["To allow humidified ambient air into the reservoir during exhalation", "To prevent exhaled gas from entering the reservoir bag and prevent ambient room air entrainment during inspiration", "To increase airway resistance during spontaneous breathing", "To atomize aerosolized bronchodilators into the patient's oral cavity"],
        "correct_index": 1,
        "explanation": "The one-way valve between the reservoir bag and mask allows oxygen from the bag into the mask during inhalation but closes during exhalation. One-way flap valves on the side ports open during exhalation to vent exhaled gas and close on inspiration to prevent dilution with room air, delivering 60-80%+ FiO2.",
        "key_points": [
            "Requires flow of 10-15 L/min to keep the reservoir bag at least one-third to one-half full at all times.",
            "If the bag collapses during inhalation, flow must be increased immediately.",
            "Delivers the highest FiO2 among low-flow devices without mechanical ventilation."
        ],
        "sample_viva_answer": "The one-way valves ensure that exhaled CO2 does not contaminate the 100% oxygen reservoir bag, and side valves prevent entrainment of room air during inspiration, maximizing delivered oxygen concentration."
    },
    {
        "id": "RT-OT-05",
        "specialty": "Respiratory Therapy",
        "topic": "Oxygen therapy",
        "difficulty": "Advanced",
        "question": "Which of the following is a primary physiological benefit provided by High-Flow Nasal Cannula (HFNC) therapy operating at 40 to 60 L/min?",
        "options": ["Generates high negative intrathoracic pressures during expiration", "Flushes anatomical dead space of exhaled CO2, delivers precise warmed/humidified gas, and generates modest PEEP", "Directly aerosolizes surfactant into subsegmental bronchi", "Acts as a closed-circuit volume-controlled ventilator"],
        "correct_index": 1,
        "explanation": "HFNC delivers heated, fully humidified gas at flow rates exceeding patient peak inspiratory demand (up to 60 L/min). Physiological benefits include continuous washout of nasopharyngeal dead space (reducing rebreathing), reduction of inspiratory resistive work, and generation of modest positive airway pressure (~2-5 cmH2O PEEP with mouth closed).",
        "key_points": [
            "Flow rates up to 60 L/min with adjustable FiO2 from 21% to 100%.",
            "Dead space CO2 washout improves ventilatory efficiency.",
            "Optimal humidification (37°C, 44 mg H2O/L) preserves mucociliary transport."
        ],
        "sample_viva_answer": "HFNC washes out nasopharyngeal dead space of expired carbon dioxide, delivers precise FiO2 matching or exceeding peak inspiratory flow, improves mucociliary clearance with humidified gas, and generates modest positive end-expiratory pressure."
    },
    {
        "id": "RT-OT-06",
        "specialty": "Respiratory Therapy",
        "topic": "Oxygen therapy",
        "difficulty": "Advanced",
        "question": "What is the phenomenon of 'absorption atelectasis' associated with breathing high concentrations of oxygen (FiO2 > 0.80) for extended periods?",
        "options": ["Alveolar rupture due to hyperbaric gas compression", "Washout of alveolar nitrogen, causing rapid absorption of alveolar oxygen into capillary blood and collapse of poorly ventilated alveoli", "Hypertrophy of goblet cells in terminal bronchioles", "Surfactant denaturing due to nitrogen toxicity"],
        "correct_index": 1,
        "explanation": "Nitrogen is relatively insoluble in blood and acts as a physiological 'splint' keeping alveoli open. When breathing high FiO2, nitrogen is washed out. Oxygen diffuses into capillary blood much faster than fresh gas enters partially obstructed units, causing the alveoli to collapse (absorption atelectasis).",
        "key_points": [
            "Nitrogen splint effect is lost during high FiO2 therapy.",
            "Commonly occurs in dependent lung regions with low V/Q ratios.",
            "Prevented by maintaining the lowest FiO2 required to achieve target SpO2 (92-96%)."
        ],
        "sample_viva_answer": "Absorption atelectasis occurs when high FiO2 washes out alveolar nitrogen. Because oxygen diffuses rapidly into capillary blood, poorly ventilated alveoli lose gas volume quickly and collapse."
    },
    {
        "id": "RT-OT-07",
        "specialty": "Respiratory Therapy",
        "topic": "Oxygen therapy",
        "difficulty": "Intermediate",
        "question": "How can a respiratory technologist distinguish a backpressure-compensated Thorpe tube flowmeter from an uncompensated flowmeter?",
        "options": ["The compensated flowmeter has a digital LED screen", "In a compensated flowmeter, the needle valve is located downstream (distal) to the tapered Thorpe tube", "In a compensated flowmeter, the float sinks below zero when connected to 50 psi", "The compensated tube has no calibrated lines"],
        "correct_index": 1,
        "explanation": "In a backpressure-compensated Thorpe tube, the needle control valve is placed downstream of the tube. This ensures that the tube remains pressurized at pipeline pressure (50 psi). When backpressure occurs from downstream equipment (e.g., nebulizers), the float still reads accurately.",
        "key_points": [
            "Compensated: Needle valve downstream of tube. Float jumps when plugged into gas outlet.",
            "Uncompensated: Needle valve upstream of tube. Reads falsely low with downstream resistance.",
            "Thorpe tube must always be kept vertical for gravity-dependent ball float accuracy."
        ],
        "sample_viva_answer": "A backpressure-compensated Thorpe tube has its needle control valve located downstream of the tapered metering tube. When connected to a 50 psi gas source, the float momentarily jumps and settles back to zero, confirming the tube is pressurized."
    },
    {
        "id": "RT-OT-08",
        "specialty": "Respiratory Therapy",
        "topic": "Oxygen therapy",
        "difficulty": "Beginner",
        "question": "Why is a Bourdon gauge flowmeter preferred over a Thorpe tube flowmeter during patient ambulance transport?",
        "options": ["Bourdon gauges generate their own oxygen supply", "A Bourdon gauge operates on gas pressure and is not gravity-dependent, remaining accurate in any physical orientation", "Bourdon gauges have built-in pulse oximetry", "Bourdon gauges deliver warm humidified oxygen automatically"],
        "correct_index": 1,
        "explanation": "Thorpe tubes rely on gravity to balance the float and must remain strictly vertical to read accurately. A Bourdon gauge relies on internal hollow curved tube uncoiling proportional to pressure, making it functional in any position during vehicle transit.",
        "key_points": [
            "Bourdon gauge: non-gravity dependent; ideal for patient transport.",
            "Thorpe tube: gravity dependent; must remain vertical; ideal for hospital wall outlets.",
            "Bourdon gauge measures pressure but is calibrated to display equivalent flow."
        ],
        "sample_viva_answer": "A Bourdon gauge is not gravity-dependent and functions accurately in any position or angle, making it the device of choice for transport cylinders and emergency ambulances where a Thorpe tube would tilt and give erroneous readings."
    },
    {
        "id": "RT-OT-09",
        "specialty": "Respiratory Therapy",
        "topic": "Oxygen therapy",
        "difficulty": "Intermediate",
        "question": "What is the structural difference between a partial rebreathing mask and a non-rebreathing mask?",
        "options": ["Partial rebreathing mask has no reservoir bag", "Partial rebreathing mask lacks one-way valves on the mask exhalation ports and between the bag and mask, allowing the first third of exhaled gas to enter the bag", "Partial rebreathing mask connects directly to wall suction", "Non-rebreathing mask cannot deliver more than 40% FiO2"],
        "correct_index": 1,
        "explanation": "A partial rebreathing mask does not have one-way valves. The first third of exhaled gas (coming from anatomical dead space and rich in O2 without significant CO2) enters the reservoir bag and is rebreathed, delivering 40-70% FiO2 at 8-15 L/min.",
        "key_points": [
            "Partial rebreather: no one-way valves; re-breathes initial anatomical dead space gas.",
            "Non-rebreather: has one-way valves; prevents rebreathing of any expired gas.",
            "Both require minimum flow of 10-15 L/min to keep bag inflated."
        ],
        "sample_viva_answer": "A partial rebreather lacks the one-way valves found on an NRB. This allows the initial portion of exhaled breath—which originated in anatomical dead space and is rich in oxygen—to enter the reservoir bag to be rebreathed."
    },
    {
        "id": "RT-OT-10",
        "specialty": "Respiratory Therapy",
        "topic": "Oxygen therapy",
        "difficulty": "Advanced",
        "question": "What is a primary clinical indication for Hyperbaric Oxygen Therapy (HBOT) administered at 2.5 to 3.0 atmospheres absolute (ATA)?",
        "options": ["Severe chronic obstructive pulmonary disease exacerbation", "Acute carbon monoxide (CO) poisoning with neurological deficits or high carboxyhemoglobin levels", "Uncontrolled acute tension pneumothorax", "Asthma exacerbation refractory to beta-2 agonists"],
        "correct_index": 1,
        "explanation": "HBOT is indicated in severe carbon monoxide poisoning, arterial gas embolism, decompression sickness, and clostridial gas gangrene. At 3 ATA of 100% O2, dissolved oxygen in plasma rises to ~6 mL/dL, which meets resting tissue metabolic demand without hemoglobin, and shortens CO-Hb half-life from ~320 minutes to ~23 minutes.",
        "key_points": [
            "Half-life of CO-Hb: room air ~320 min; 100% NRB ~80 min; HBOT (3 ATA) ~23 min.",
            "Dissolved plasma oxygen provides adequate tissue oxygenation independent of hemoglobin.",
            "Contraindication: untreated tension pneumothorax."
        ],
        "sample_viva_answer": "Severe carbon monoxide poisoning is a classic indication for hyperbaric oxygen therapy. It rapidly displaces CO from hemoglobin, dramatically reducing carboxyhemoglobin half-life to under 25 minutes, and delivers abundant dissolved plasma oxygen to ischemic tissues."
    },
    {
        "id": "RT-OT-11",
        "specialty": "Respiratory Therapy",
        "topic": "Oxygen therapy",
        "difficulty": "Intermediate",
        "question": "What is the air-to-oxygen entrainment ratio for a Venturi mask calibrated to deliver 40% FiO2?",
        "options": ["25:1", "8:1", "3:1", "1:1"],
        "correct_index": 2,
        "explanation": "Air/O2 ratio = (100 - FiO2) / (FiO2 - 21). For 40%: (100 - 40) / (40 - 21) = 60 / 19 = ~3.16:1. For every 1 L/min of oxygen flow, approximately 3 L/min of room air is entrained, giving an air-to-oxygen ratio of 3:1 (total factor = 4).",
        "key_points": [
            "Formula: Air:O2 ratio = (100 - FiO2) / (FiO2 - 21).",
            "24% FiO2 = 25:1 ratio (factor 26).",
            "28% FiO2 = 10:1 ratio (factor 11).",
            "40% FiO2 = 3:1 ratio (factor 4). Total flow = O2 flow * 4."
        ],
        "sample_viva_answer": "For 40% FiO2, the air-to-oxygen entrainment ratio is 3:1. This means for every 1 L/min of piped oxygen, 3 L/min of room air is entrained through the calibrated ports, multiplying total flow by four."
    },
    {
        "id": "RT-OT-12",
        "specialty": "Respiratory Therapy",
        "topic": "Oxygen therapy",
        "difficulty": "Beginner",
        "question": "What is the recommended target oxygen saturation (SpO2) range for a patient with severe chronic hypercapnic respiratory failure (e.g., advanced COPD) receiving controlled oxygen therapy?",
        "options": ["80% to 84%", "88% to 92%", "96% to 100%", "99% to 100%"],
        "correct_index": 1,
        "explanation": "In patients vulnerable to hypercapnia (COPD with chronic CO2 retention), excessive oxygen therapy blunts hypoxic drive, worsens V/Q mismatch via reversal of hypoxic vasoconstriction, and causes the Haldane effect. International guidelines recommend a targeted SpO2 of 88% to 92%.",
        "key_points": [
            "Target SpO2 for hypercapnic risk patients: 88% to 92%.",
            "Target SpO2 for most acutely ill patients without hypercapnic risk: 92% to 96%.",
            "Venturi mask or low-flow nasal prongs titrated to maintain 88-92%."
        ],
        "sample_viva_answer": "In patients with severe COPD at risk of hypercapnic respiratory failure, the target SpO2 range is 88% to 92% to prevent acute carbon dioxide retention from oxygen-induced worsening of V/Q mismatch and the Haldane effect."
    }
]

RT_VF_QUESTIONS = [
    {
        "id": "RT-VF-01",
        "specialty": "Respiratory Therapy",
        "topic": "Ventilator fundamentals",
        "difficulty": "Beginner",
        "question": "What does PEEP (Positive End-Expiratory Pressure) primarily achieve in mechanical ventilation?",
        "options": ["Increases peak inspiratory flow velocity", "Maintains supra-atmospheric alveolar pressure at end-expiration to prevent alveolar collapse", "Decreases anatomical dead space to zero", "Permits spontaneous exhalation below barometric baseline"],
        "correct_index": 1,
        "explanation": "PEEP maintains positive alveolar pressure at the end of exhalation. This recruits collapsed or unstable alveoli, increases functional residual capacity (FRC), improves oxygenation, and prevents atelectrauma caused by cyclical opening and closing of lung units.",
        "key_points": [
            "Prevents end-expiratory alveolar de-recruitment (atelectasis).",
            "Increases Functional Residual Capacity (FRC) and improves ventilation-perfusion matching.",
            "Excessive PEEP can cause barotrauma, decreased venous return, and reduced cardiac output."
        ],
        "sample_viva_answer": "PEEP prevents alveolar collapse at end-expiration, restoring and maintaining functional residual capacity (FRC) to enhance arterial oxygenation. Caution is needed as excessive PEEP compromises venous return and blood pressure."
    },
    {
        "id": "RT-VF-02",
        "specialty": "Respiratory Therapy",
        "topic": "Ventilator fundamentals",
        "difficulty": "Advanced",
        "question": "During volume-controlled ventilation, an acute rise in Peak Airway Pressure (Ppeak) with a stable Plateau Pressure (Pplat) indicates which clinical problem?",
        "options": ["Decreased lung compliance (e.g., worsening pulmonary edema or ARDS)", "Tension pneumothorax", "Increased airway resistance (e.g., bronchospasm, mucus plug, or biting the ETT)", "Chest wall rigidity"],
        "correct_index": 2,
        "explanation": "Transairway pressure is the difference between Peak Pressure (Ppeak) and Plateau Pressure (Pplat). When Ppeak increases while Pplat remains constant, airway resistance (Raw) has risen (e.g., secretions, bronchospasm, kinked endotracheal tube). In contrast, a rise in both Ppeak and Pplat indicates decreased compliance.",
        "key_points": [
            "Ppeak reflects both airway resistance and respiratory system compliance.",
            "Pplat (measured during an end-inspiratory pause) reflects static compliance of lung and chest wall.",
            "Widened gradient (Ppeak - Pplat) = elevated airway resistance.",
            "Both elevated with parallel difference = worsening respiratory compliance."
        ],
        "sample_viva_answer": "An elevated peak pressure with an unchanged plateau pressure indicates an increase in resistive work—such as an endotracheal tube kink, bronchospasm, or secretions in the airway. It is not a parenchymal compliance issue."
    },
    {
        "id": "RT-VF-03",
        "specialty": "Respiratory Therapy",
        "topic": "Ventilator fundamentals",
        "difficulty": "Intermediate",
        "question": "How is Static Respiratory System Compliance (Cstat) calculated at the bedside on a mechanically ventilated patient?",
        "options": ["Cstat = Tidal Volume / (Ppeak - Pplat)", "Cstat = Tidal Volume / (Pplat - Total PEEP)", "Cstat = (Ppeak - Total PEEP) / Flow Rate", "Cstat = Minute Ventilation / (Pplat - Ppeak)"],
        "correct_index": 1,
        "explanation": "Static compliance measures the distensibility of the lungs and thoracic cage at zero gas flow. Cstat = Exhaled Tidal Volume / (Plateau Pressure - Total PEEP). Normal values in mechanically ventilated adult patients are 50 to 80 mL/cmH2O.",
        "key_points": [
            "Requires an end-inspiratory pause maneuver (0.5 - 1.0 s) to measure Pplat.",
            "Decreased in ARDS, pulmonary edema, atelectasis, pneumothorax, and abdominal distension.",
            "Dynamic compliance (Cdyn) uses Ppeak and includes resistive pressure."
        ],
        "sample_viva_answer": "Static compliance is calculated as tidal volume divided by the driving pressure, which is plateau pressure minus total PEEP. Normal values in ventilated adults are 50 to 80 mL/cmH2O."
    },
    {
        "id": "RT-VF-04",
        "specialty": "Respiratory Therapy",
        "topic": "Ventilator fundamentals",
        "difficulty": "Beginner",
        "question": "In standard Volume Control (VC) ventilation, what variable serves as the primary 'cycle variable' that terminates inspiration?",
        "options": ["Airway pressure threshold", "Delivered preset tidal volume (or inspiratory time)", "Patient inspiratory flow drop to 25%", "Expiratory carbon dioxide concentration"],
        "correct_index": 1,
        "explanation": "In volume-controlled ventilation, inspiration ends (cycles into exhalation) once the pre-set tidal volume is delivered (volume-cycled) or after a set inspiratory time corresponding to that volume. Pressure varies depending on patient compliance and resistance.",
        "key_points": [
            "Trigger: initiates inspiration (time or patient effort).",
            "Limit: max value reached during inspiration (flow or volume).",
            "Cycle: variable that terminates inspiration (volume in VC, time in PC, flow in PSV)."
        ],
        "sample_viva_answer": "Volume Control ventilation is volume-cycled (or time-cycled at preset volume and flow rate). Inspiration terminates once the dialed tidal volume has been delivered into the breathing circuit."
    },
    {
        "id": "RT-VF-05",
        "specialty": "Respiratory Therapy",
        "topic": "Ventilator fundamentals",
        "difficulty": "Advanced",
        "question": "How does a bedside clinician detect and measure Auto-PEEP (intrinsic PEEP / dynamic hyperinflation) on a mechanical ventilator?",
        "options": ["Perform an end-inspiratory pause maneuver", "Perform an end-expiratory occlusion/hold maneuver just before the next scheduled mandatory breath", "Increase the inspiratory flow rate to 100 L/min", "Observe the peak pressure alarm gauge during suctioning"],
        "correct_index": 1,
        "explanation": "Auto-PEEP is measured by performing an end-expiratory hold maneuver. Closing the inspiratory and expiratory valves at end-exhalation allows trapped alveolar gas pressure to equilibrate with the ventilator pressure transducer, displaying total PEEP. Auto-PEEP = Total PEEP - Set PEEP.",
        "key_points": [
            "Auto-PEEP occurs when expiratory time (Te) is shorter than the time needed for full lung deflation.",
            "Causes hemodynamic instability, increased work of breathing, and barotrauma.",
            "Management: decrease respiratory rate, increase inspiratory flow (shorter Ti), prolong Te."
        ],
        "sample_viva_answer": "Auto-PEEP is quantified by performing an end-expiratory hold maneuver. Trapped alveolar gas pressure equilibrates throughout the circuit, displaying total PEEP. Subtracting set PEEP reveals intrinsic Auto-PEEP."
    },
    {
        "id": "RT-VF-06",
        "specialty": "Respiratory Therapy",
        "topic": "Ventilator fundamentals",
        "difficulty": "Intermediate",
        "question": "What ventilatory strategy is recommended for a mechanically ventilated patient with severe status asthmaticus and dynamic hyperinflation?",
        "options": ["High respiratory rate (>25 bpm) and short expiratory time", "Low respiratory rate, prolonged expiratory time (I:E ratio 1:3 or 1:4), and permissive hypercapnia", "Zero PEEP and high tidal volumes (>10 mL/kg)", "Inverse ratio ventilation (I:E 2:1)"],
        "correct_index": 1,
        "explanation": "Severe airflow obstruction requires prolonged expiratory time (Te) to allow complete exhalation and minimize breath-stacking. The ventilator strategy uses low respiratory rates (10-12 bpm), high inspiratory flows (short Ti), and permissive hypercapnia (tolerating respiratory acidosis as long as pH > 7.20).",
        "key_points": [
            "Primary goal: minimize dynamic hyperinflation and Auto-PEEP.",
            "Target plateau pressure < 30 cmH2O.",
            "Permissive hypercapnia is safer than aggressive ventilation that risks barotrauma."
        ],
        "sample_viva_answer": "For status asthmaticus, the strategy involves a low respiratory rate, high peak inspiratory flow, prolonged expiratory time (I:E ratio 1:3 to 1:4), and permissive hypercapnia to prevent dangerous air-trapping and tension pneumothorax."
    },
    {
        "id": "RT-VF-07",
        "specialty": "Respiratory Therapy",
        "topic": "Ventilator fundamentals",
        "difficulty": "Beginner",
        "question": "What parameter terminates the inspiratory phase (cycling mechanism) during Pressure Support Ventilation (PSV)?",
        "options": ["Elapsed mandatory inspiratory time", "Flow cycling: inspiratory flow drops to a pre-set percentage (e.g., 25%) of peak inspiratory flow", "Target tidal volume reached exactly", "Diaphragmatic electromyogram cessation"],
        "correct_index": 1,
        "explanation": "Pressure Support Ventilation (PSV) is patient-triggered, pressure-limited, and flow-cycled. The ventilator pressurizes the circuit to the dialed support level; when the patient's inspiratory flow decays to a set threshold (typically 25% of peak flow), the ventilator cycles into exhalation.",
        "key_points": [
            "PSV is a spontaneous, assisted mode of ventilation.",
            "Patient controls rate, inspiratory time, and tidal volume.",
            "Early or delayed cycling can cause patient-ventilator asynchrony."
        ],
        "sample_viva_answer": "Pressure Support Ventilation is flow-cycled. As the patient's inspiratory demand subsides and flow decays to a threshold (usually 25% of peak inspiratory flow), the ventilator terminates inspiration and opens the exhalation valve."
    },
    {
        "id": "RT-VF-08",
        "specialty": "Respiratory Therapy",
        "topic": "Ventilator fundamentals",
        "difficulty": "Intermediate",
        "question": "If a mechanically ventilated patient suddenly triggers a continuous High Peak Airway Pressure alarm and develops acute severe distress, what is the mandatory immediate first action by the technologist or clinician?",
        "options": ["Silence the alarm and increase the high pressure limit to 60 cmH2O", "Immediately disconnect the patient from the ventilator and initiate manual bag-valve ventilation with 100% O2 to feel lung compliance", "Order an immediate stat chest CT scan", "Administer intravenous neuromuscular blockade"],
        "correct_index": 1,
        "explanation": "The universal first step in acute ventilator emergencies is disconnecting the patient from the machine and initiating manual bag-mask ventilation with 100% O2. This immediately identifies whether the problem is in the patient (e.g., tension pneumothorax, severe bronchospasm, tube obstruction) or in the ventilator circuit (e.g., valve failure).",
        "key_points": [
            "Disconnect and manual bag ventilation with 100% FiO2.",
            "Assesses hand-feel compliance and airway resistance directly.",
            "Check for tension pneumothorax (tracheal deviation, absent breath sounds, hypotension)."
        ],
        "sample_viva_answer": "In any sudden high pressure crisis with patient distress, immediately disconnect the patient from the ventilator and bag manually with 100% oxygen. This determines if resistance is inside the patient or the ventilator machine, while maintaining ventilation."
    },
    {
        "id": "RT-VF-09",
        "specialty": "Respiratory Therapy",
        "topic": "Ventilator fundamentals",
        "difficulty": "Advanced",
        "question": "What is the phenomenon of 'double triggering' asynchrony on ventilator scalar graphics?",
        "options": ["Two mandatory breaths delivered during a single patient effort because the set inspiratory time is shorter than the patient's neural inspiratory time", "The exhalation valve sticking closed during exhalation", "Failure of the patient to trigger the ventilator due to muscle weakness", "Oscillation of the pressure curve caused by condensation water in tubing"],
        "correct_index": 0,
        "explanation": "Double triggering occurs when the patient's neural inspiratory drive remains active when the ventilator terminates the mechanical breath (set Ti < neural Ti). The persistent inspiratory effort immediately triggers a second breath, resulting in dangerous breath stacking and high tidal volumes.",
        "key_points": [
            "Occurs frequently in ARDS with high ventilatory drive.",
            "Can cause significant volutrauma due to stacked tidal volume.",
            "Managed by increasing inspiratory time, adjusting tidal volume, or deepening sedation."
        ],
        "sample_viva_answer": "Double triggering is a patient-ventilator asynchrony where the patient's neural effort outlasts the ventilator's inspiratory time, causing the ventilator to immediately deliver a second breath, leading to dangerous breath stacking."
    },
    {
        "id": "RT-VF-10",
        "specialty": "Respiratory Therapy",
        "topic": "Ventilator fundamentals",
        "difficulty": "Beginner",
        "question": "In Non-Invasive Positive Pressure Ventilation (NIPPV) using BiPAP mode, what does the difference between IPAP (Inspiratory Positive Airway Pressure) and EPAP (Expiratory Positive Airway Pressure) represent?",
        "options": ["Mean Airway Pressure", "Pressure Support level (which determines tidal volume and CO2 clearance)", "Total Auto-PEEP", "Inspiratory to Expiratory time ratio"],
        "correct_index": 1,
        "explanation": "The pressure gradient (IPAP minus EPAP) is the Pressure Support level. This pressure difference drives inspiratory gas flow, expands the lungs, and determines tidal volume, thereby clearing carbon dioxide. EPAP acts identically to PEEP, recruiting alveoli and improving oxygenation.",
        "key_points": [
            "Pressure Support = IPAP - EPAP.",
            "Increasing IPAP improves ventilation and lowers PaCO2.",
            "Increasing EPAP improves oxygenation and functional residual capacity."
        ],
        "sample_viva_answer": "The difference between IPAP and EPAP represents the effective Pressure Support. This pressure gradient dictates the tidal volume delivered to the patient and governs carbon dioxide elimination."
    },
    {
        "id": "RT-VF-11",
        "specialty": "Respiratory Therapy",
        "topic": "Ventilator fundamentals",
        "difficulty": "Advanced",
        "question": "Which of the following lung-protective mechanical ventilation parameters is supported by the ARDSNet protocol for acute respiratory distress syndrome?",
        "options": ["Tidal volume 10-12 mL/kg of actual body weight, plateau pressure unlimited", "Tidal volume 4-8 mL/kg of Predicted (Ideal) Body Weight (PBW) and maintaining Plateau Pressure < 30 cmH2O", "Zero PEEP and high peak pressures", "Mandatory hyperventilation to achieve PaCO2 < 30 mmHg"],
        "correct_index": 1,
        "explanation": "The landmark ARDSNet trial established low tidal volume ventilation (4-8 mL/kg of predicted body weight, starting at 6 mL/kg PBW) and limiting static plateau pressure to <= 30 cmH2O to prevent volutrauma, barotrauma, and biotrauma.",
        "key_points": [
            "Tidal volume based on Predicted Body Weight (PBW), not actual scale weight.",
            "Plateau pressure target < 30 cmH2O.",
            "Titrated PEEP according to PEEP/FiO2 tables to maintain open lung."
        ],
        "sample_viva_answer": "The ARDSNet lung-protective protocol mandates a low tidal volume of 4 to 8 mL/kg of predicted body weight and a plateau pressure strictly below 30 cmH2O to mitigate ventilator-induced lung injury."
    },
    {
        "id": "RT-VF-12",
        "specialty": "Respiratory Therapy",
        "topic": "Ventilator fundamentals",
        "difficulty": "Intermediate",
        "question": "How is the Rapid Shallow Breathing Index (RSBI / Tobin Index) calculated, and what threshold value predicts successful weaning and extubation?",
        "options": ["RSBI = PaO2 / FiO2 (> 200)", "RSBI = Respiratory Rate (breaths/min) / Tidal Volume in Liters (< 105)", "RSBI = Tidal Volume / Plateau Pressure (< 50)", "RSBI = Minute Ventilation * Respiratory Rate (> 80)"],
        "correct_index": 1,
        "explanation": "RSBI = f / Vt (frequency in breaths/min divided by tidal volume in liters), measured during 1 minute of spontaneous breathing without pressure support. An RSBI < 105 breaths/min/L strongly predicts successful weaning from mechanical ventilation.",
        "key_points": [
            "Formula: RSBI = f / Vt (L).",
            "Values < 105 predict successful extubation.",
            "Values > 105 indicate rapid, shallow breathing and high risk of extubation failure."
        ],
        "sample_viva_answer": "The Rapid Shallow Breathing Index equals spontaneous respiratory rate divided by tidal volume in liters. An RSBI under 105 breaths per minute per liter is an established predictor of successful weaning from mechanical ventilation."
    }
]

RT_RE_QUESTIONS = [
    {
        "id": "RT-RE-01",
        "specialty": "Respiratory Therapy",
        "topic": "Respiratory equipment",
        "difficulty": "Beginner",
        "question": "What is the primary function of a Heat and Moisture Exchanger (HME) filter placed on a mechanically ventilated patient?",
        "options": ["To measure real-time exhaled carbon dioxide tension", "To capture exhaled heat and moisture and return it during the subsequent inhalation", "To generate positive expiratory threshold resistance", "To deliver nebulized bronchodilators continuously"],
        "correct_index": 1,
        "explanation": "An HME (artificial nose) acts as a passive humidifier. It contains a hygroscopic and thermal matrix that captures heat and moisture from the patient's exhaled gas and returns it to warm and humidify the dry incoming gas during inspiration.",
        "key_points": [
            "Prevents mucosal drying and thick secretions when the upper airway is bypassed by an ETT or tracheostomy.",
            "Should be replaced if visibly soiled with secretions or blood.",
            "Contraindicated in thick copious secretions, hypothermia, or large tidal volume leaks."
        ],
        "sample_viva_answer": "An HME captures heat and humidity from the patient's exhaled breath and returns it on inhalation, acting as an artificial nose when the natural humidification of the nasopharynx is bypassed by an endotracheal tube."
    },
    {
        "id": "RT-RE-02",
        "specialty": "Respiratory Therapy",
        "topic": "Respiratory equipment",
        "difficulty": "Intermediate",
        "question": "Which type of aerosol generator produces fine medication particles using high-frequency piezoelectric crystal vibrations without requiring compressed gas?",
        "options": ["Pneumatic jet nebulizer", "Ultrasonic / Vibrating mesh nebulizer", "Metered-dose inhaler with spacer", "Dry powder inhaler (DPI)"],
        "correct_index": 1,
        "explanation": "Ultrasonic and vibrating mesh nebulizers utilize piezoelectric elements vibrating at high frequency (1-3 MHz for ultrasonic, or micro-aperture mesh) to generate aerosol clouds without needing pressurized medical gas lines.",
        "key_points": [
            "Vibrating mesh devices have minimal residual dead volume and high delivery efficiency.",
            "Do not introduce extra gas flow into ventilator breathing circuits, preventing tidal volume disturbances.",
            "Ultrasonic nebulizers can heat solutions and degrade heat-sensitive medications like suspension proteins."
        ],
        "sample_viva_answer": "Vibrating mesh and ultrasonic nebulizers use piezoelectric crystal elements vibrating at high frequency. Vibrating mesh technology is preferred in ventilator circuits because it does not alter flow or volume delivery."
    },
    {
        "id": "RT-RE-03",
        "specialty": "Respiratory Therapy",
        "topic": "Respiratory equipment",
        "difficulty": "Intermediate",
        "question": "What is the recommended safe endotracheal tube (ETT) cuff pressure range to prevent both tracheal mucosal ischemic necrosis and aspiration leaks?",
        "options": ["5 to 10 cmH2O", "20 to 30 cmH2O (or 15 to 22 mmHg)", "45 to 55 cmH2O", "70 to 80 cmH2O"],
        "correct_index": 1,
        "explanation": "Tracheal capillary perfusion pressure is approximately 25-30 mmHg (~30-35 cmH2O). Maintaining ETT cuff pressure between 20-30 cmH2O (15-22 mmHg) prevents mucosal ischemia, tracheal stenosis, and necrosis while providing an effective seal against micro-aspiration.",
        "key_points": [
            "Safe range: 20-30 cmH2O (measured with a calibrated cuff pressure manometer).",
            "> 30 cmH2O: compromises mucosal blood flow, risking ulceration and stenosis.",
            "< 20 cmH2O: permits leakage and increases Ventilator-Associated Pneumonia (VAP) risk."
        ],
        "sample_viva_answer": "The recommended ETT cuff pressure is 20 to 30 cmH2O. This pressure creates an adequate tracheal seal against micro-aspiration while remaining below mucosal capillary perfusion pressure to prevent tracheal ischemic injury."
    },
    {
        "id": "RT-RE-04",
        "specialty": "Respiratory Therapy",
        "topic": "Respiratory equipment",
        "difficulty": "Beginner",
        "question": "What is a major clinical advantage of using a Closed In-Line Suction System on a mechanically ventilated patient with high PEEP?",
        "options": ["Eliminates the need for sterile suction catheters entirely", "Allows endotracheal suctioning without disconnecting the patient, preventing loss of PEEP, alveolar derecruitment, and room aerosolization", "Increases delivered tidal volumes by 50%", "Replaces the need for subglottic suctioning tubes"],
        "correct_index": 1,
        "explanation": "A closed suction catheter resides within a sterile plastic sheath attached to the ventilator circuit. Suctioning without disconnecting maintains ventilator PEEP, prevents hypoxia and alveolar collapse in severe ARDS, and minimizes environmental contamination.",
        "key_points": [
            "Maintains continuous PEEP and circuit integrity.",
            "Reduces environmental aerosolization and cross-contamination.",
            "Limits suction duration to <= 10-15 seconds with pre-oxygenation."
        ],
        "sample_viva_answer": "A closed suction system allows tracheal suctioning without breaking the breathing circuit, preserving therapeutic PEEP to avoid alveolar derecruitment, and protecting staff from infectious aerosols."
    },
    {
        "id": "RT-RE-05",
        "specialty": "Respiratory Therapy",
        "topic": "Respiratory equipment",
        "difficulty": "Intermediate",
        "question": "A peak flow meter (e.g., Wright peak flow meter) is primarily designed to assess which clinical lung parameter in an asthma patient?",
        "options": ["Forced Vital Capacity (FVC)", "Peak Expiratory Flow Rate (PEFR)", "Diffusing capacity of carbon monoxide (DLCO)", "Functional Residual Capacity (FRC)"],
        "correct_index": 1,
        "explanation": "Peak flow meters measure Peak Expiratory Flow Rate (PEFR)—the maximum flow rate achieved during a forced expiration starting from total lung capacity. It is an established bedside tool for monitoring acute asthma severity and bronchodilator response.",
        "key_points": [
            "Measured in liters per minute (L/min).",
            "Asthma action plan zones: Green (80-100% of personal best), Yellow (50-80%), Red (< 50%).",
            "Effort-dependent maneuver requiring patient instruction."
        ],
        "sample_viva_answer": "A peak flow meter measures Peak Expiratory Flow Rate (PEFR) in liters per minute, reflecting the caliber of large central airways and helping monitor airway obstruction in asthmatic patients."
    },
    {
        "id": "RT-RE-06",
        "specialty": "Respiratory Therapy",
        "topic": "Respiratory equipment",
        "difficulty": "Advanced",
        "question": "In a heated pass-over humidifier system (e.g., Fisher & Paykel MR850), what is the purpose of using heated-wire breathing circuits?",
        "options": ["To heat the gas to 60°C to sterilize bacteria", "To prevent condensation ('rain-out') in the breathing tubing by maintaining uniform gas temperature from chamber to Y-piece", "To generate electrical nebulization", "To calibrate the expiratory flow sensor continuously"],
        "correct_index": 1,
        "explanation": "As saturated warm gas moves from the humidifier toward the patient, ambient room cooling causes condensation (rain-out) inside unheated tubing. Heated wires embedded within the circuit maintain temperature, preventing rain-out and bacterial reservoir formation.",
        "key_points": [
            "Prevents tubing condensation ('rain-out') and circuit occlusion.",
            "Dual-heated wire circuits heat both inspiratory and expiratory limbs.",
            "Delivers 37°C at 100% relative humidity (44 mg H2O/L) at the airway."
        ],
        "sample_viva_answer": "Heated-wire circuits maintain a constant gas temperature between the humidification chamber and the patient Y-piece, preventing gas cooling and liquid condensation (rain-out) inside the tubing."
    },
    {
        "id": "RT-RE-07",
        "specialty": "Respiratory Therapy",
        "topic": "Respiratory equipment",
        "difficulty": "Beginner",
        "question": "How does a colorimetric end-tidal CO2 detector indicate successful endotracheal tube placement inside the trachea?",
        "options": ["Changes from yellow to blue", "Changes from purple (low CO2) to yellow (exhaled CO2 > 2%) on successive exhalations", "Flashes a red LED light", "Emits an audible beep at 40 cmH2O"],
        "correct_index": 1,
        "explanation": "Colorimetric CO2 detectors use a pH-sensitive chemical indicator paper. Room air and esophageal gas (low CO2) show purple. Exhaled alveolar gas containing CO2 forms carbonic acid, lowering pH and turning the paper yellow. A persistent yellow change over 6 breaths confirms tracheal intubation.",
        "key_points": [
            "Purple = Check (< 0.5% CO2); Tan = Caution (0.5 - 2% CO2); Yellow = Yes (> 2% CO2).",
            "Can give false negative in cardiac arrest (absence of pulmonary blood flow to deliver CO2).",
            "Must verify color change across at least 6 consecutive breaths."
        ],
        "sample_viva_answer": "A colorimetric detector changes from purple to yellow upon exposure to exhaled carbon dioxide. A persistent yellow change across multiple exhalations confirms correct placement in the trachea."
    },
    {
        "id": "RT-RE-08",
        "specialty": "Respiratory Therapy",
        "topic": "Respiratory equipment",
        "difficulty": "Intermediate",
        "question": "What is the critical function of the 'obturator' included with a cuffed tracheostomy tube set?",
        "options": ["Locks the inner cannula in place during positive pressure ventilation", "Provides a rounded, smooth leading edge during tube insertion to minimize tissue trauma, and is removed immediately after insertion", "Acts as an in-line oxygen delivery jet", "Maintains cuff inflation automatically"],
        "correct_index": 1,
        "explanation": "The obturator is placed inside the outer cannula prior to insertion. Its smooth, rounded tip extends beyond the distal end of the cannula, minimizing tracheal trauma and false passage creation. It is removed immediately once the tube is in place to allow breathing.",
        "key_points": [
            "Used only during insertion to provide a blunt, atraumatic tip.",
            "Must be removed immediately following insertion to clear the airway lumen.",
            "Kept at the patient's bedside at all times for emergency re-cannulation."
        ],
        "sample_viva_answer": "The obturator provides a smooth, rounded guide tip that extends past the outer cannula to prevent tissue trauma during insertion into the trachea. It is removed immediately after tube placement."
    },
    {
        "id": "RT-RE-09",
        "specialty": "Respiratory Therapy",
        "topic": "Respiratory equipment",
        "difficulty": "Beginner",
        "question": "What safety feature is incorporated into adult manual resuscitation bags (Ambu bags) to prevent accidental pulmonary barotrauma?",
        "options": ["Flow-triggered demand regulator", "Pressure-limiting pop-off valve set to release at approximately 40 to 45 cmH2O", "Mercury barometer circuit switch", "Solenoid shut-off valve"],
        "correct_index": 1,
        "explanation": "Most self-inflating resuscitation bags include a spring-loaded pressure relief (pop-off) valve calibrated to vent gas if circuit pressure exceeds 40-45 cmH2O, protecting fragile lung parenchyma from barotrauma during manual ventilation.",
        "key_points": [
            "Pop-off valve typically opens at 40-45 cmH2O.",
            "Can be overridden with a clip or manual override if high pressures are clinically required.",
            "Includes a non-rebreathing patient valve and oxygen reservoir bag."
        ],
        "sample_viva_answer": "Manual resuscitation bags feature a pressure-limiting pop-off valve calibrated at approximately 40 cmH2O that vents excessive pressure into ambient air to prevent barotrauma during emergency bagging."
    },
    {
        "id": "RT-RE-10",
        "specialty": "Respiratory Therapy",
        "topic": "Respiratory equipment",
        "difficulty": "Intermediate",
        "question": "How do oscillatory Positive Expiratory Pressure (OPEP) devices, such as the Flutter or Acapella, assist in airway clearance?",
        "options": ["They administer pressurized bronchodilators into alveoli", "They generate positive expiratory pressure and high-frequency airflow oscillations that vibrate airway walls and loosen retained secretions", "They create negative suction pressure during exhalation", "They deliver synchronized electrical impulses to the diaphragm"],
        "correct_index": 1,
        "explanation": "OPEP devices combine positive expiratory pressure (stenting open collapsable airways) with rapid pressure oscillations (10-30 Hz). These vibratory shockwaves decrease sputum viscosity and shear secretions from bronchial walls, facilitating mobilization by coughing.",
        "key_points": [
            "Flutter: steel ball in a cone; gravity-dependent; requires upright posture.",
            "Acapella: counterweighted lever and magnet; non-gravity dependent; usable in any position.",
            "Widely used in cystic fibrosis, bronchiectasis, and chronic bronchitis."
        ],
        "sample_viva_answer": "Oscillatory PEP devices create positive expiratory pressure to stent airways open while generating vibratory oscillations that decrease sputum viscosity and detach secretions from bronchial walls for easier expectoration."
    },
    {
        "id": "RT-RE-11",
        "specialty": "Respiratory Therapy",
        "topic": "Respiratory equipment",
        "difficulty": "Advanced",
        "question": "What is the operating principle of a paramagnetic oxygen analyzer used in modern respiratory and anesthesia equipment?",
        "options": ["Chemical reduction of gold electrodes", "Oxygen molecules are attracted into a magnetic field due to unpaired outer electrons, creating measurable physical displacement or pressure changes", "Absorption of infrared light at 4.26 micrometers", "Thermal cooling of a platinum wire"],
        "correct_index": 1,
        "explanation": "Oxygen is paramagnetic because it has two unpaired electrons in its outer molecular orbital, causing it to be attracted into magnetic fields (unlike nitrogen and CO2, which are diamagnetic). Paramagnetic sensors measure this magnetic deflection or pressure pulsation, offering rapid response and long sensor lifespan.",
        "key_points": [
            "Paramagnetic: O2 has unpaired outer electrons attracted to magnetic fields.",
            "Fast response time; does not deplete like galvanic chemical fuel cells.",
            "Used for breath-by-breath rapid FiO2 and FeO2 analysis."
        ],
        "sample_viva_answer": "Paramagnetic analyzers exploit oxygen's unique paramagnetic property, which stems from unpaired electrons attracted into a magnetic field. This creates measurable pressure differentials that correlate precisely with oxygen concentration."
    },
    {
        "id": "RT-RE-12",
        "specialty": "Respiratory Therapy",
        "topic": "Respiratory equipment",
        "difficulty": "Intermediate",
        "question": "What is a Wright Respirometer used for at the bedside of an extubation candidate?",
        "options": ["Measuring arterial blood gases continuously", "Measuring spontaneous minute volume, tidal volume, and slow vital capacity through a rotating vane mechanism", "Detecting subglottic secretions", "Monitoring peak inspiratory flow velocity"],
        "correct_index": 1,
        "explanation": "A Wright respirometer is a compact mechanical flow-integrating instrument that uses a low-inertia rotating vane connected via gear trains to calibrated dials. It measures spontaneous tidal volume and minute volume at the bedside to assess readiness for extubation.",
        "key_points": [
            "Mechanical rotating vane instrument.",
            "Measures spontaneous Tidal Volume (Vt) and Minute Volume (Ve).",
            "Over-reads at very high flow rates; under-reads at very low flow rates."
        ],
        "sample_viva_answer": "A Wright respirometer uses a precision rotating vane to measure exhaled gas volumes. It is used at the bedside to accurately evaluate a patient's spontaneous tidal volume and minute ventilation prior to extubation."
    }
]

print(f"Generated {len(RT_AP_QUESTIONS)} RT-AP, {len(RT_OT_QUESTIONS)} RT-OT, {len(RT_VF_QUESTIONS)} RT-VF, {len(RT_RE_QUESTIONS)} RT-RE.")

# =========================================================================
# ANAESTHESIA TECHNOLOGY (48 questions: 4 topics x 12 questions)
# =========================================================================

AT_EI_QUESTIONS = [
    {
        "id": "AT-EI-01",
        "specialty": "Anaesthesia Technology",
        "topic": "Anaesthesia equipment identification",
        "difficulty": "Beginner",
        "question": "Which part of the circle breathing system contains soda lime or calcium hydroxide granules to remove carbon dioxide from exhaled gas?",
        "options": ["Vaporizer manifold", "Carbon dioxide absorber canister", "Adjustable Pressure Limiting (APL) valve", "Active gas scavenging interface"],
        "correct_index": 1,
        "explanation": "The CO2 absorber canister contains chemical absorbents such as soda lime (sodium hydroxide and calcium hydroxide) with ethyl violet indicator that chemically reacts with and removes exhaled carbon dioxide, allowing safe rebreathing of volatile anaesthetic agents.",
        "key_points": [
            "Soda lime neutralization produces heat, water, and calcium carbonate.",
            "Ethyl violet turns purple when pH drops below 10.3, indicating absorbent exhaustion.",
            "Can cause compound A generation with Sevoflurane or carbon monoxide with Desflurane if desiccated."
        ],
        "sample_viva_answer": "The carbon dioxide absorber canister contains soda lime granules which chemically absorb exhaled CO2 in an exothermic reaction, turning purple via ethyl violet indicator when exhausted."
    },
    {
        "id": "AT-EI-02",
        "specialty": "Anaesthesia Technology",
        "topic": "Anaesthesia equipment identification",
        "difficulty": "Advanced",
        "question": "Why does a modern variable-bypass vaporizer require an internal temperature-compensation bimetallic strip or mechanism?",
        "options": ["To heat the liquid anaesthetic to boiling point", "To maintain constant anesthetic vapor output as latent heat of vaporization cools the liquid agent", "To prevent condensation of pipeline nitrous oxide", "To regulate the electronic solenoid valves during power outages"],
        "correct_index": 1,
        "explanation": "As liquid volatile anaesthetic vaporizes, it consumes latent heat of vaporization, causing the temperature of remaining liquid to drop and lowering its saturated vapor pressure. The bimetallic strip flexes as temperature drops to divert a greater proportion of carrier gas through the vaporizing chamber, maintaining a steady output concentration.",
        "key_points": [
            "Prevents drop in delivered concentration as agent cools during use.",
            "Agent-specific design because each volatile agent has a distinct saturated vapor pressure (e.g., Isoflurane ~238 mmHg, Sevoflurane ~160 mmHg at 20°C).",
            "Desflurane requires a heated, pressurized Tec 6 vaporizer due to high vapor pressure (669 mmHg at 20°C)."
        ],
        "sample_viva_answer": "Evaporation cools the liquid agent, reducing vapor pressure. A bimetallic strip acts as a temperature-compensating valve, flexing to direct more carrier gas through the vaporizing chamber as temperature drops to deliver a constant dialed concentration."
    },
    {
        "id": "AT-EI-03",
        "specialty": "Anaesthesia Technology",
        "topic": "Anaesthesia equipment identification",
        "difficulty": "Advanced",
        "question": "Why does a Desflurane Tec 6 vaporizer require electrical heating to 39°C and pressurization to 2 atmospheres (1500 mmHg)?",
        "options": ["Desflurane is an explosive gas that needs catalytic decomposition", "Desflurane has a boiling point of 22.8°C near room temperature and high vapor pressure (669 mmHg at 20°C), which would cause uncontrolled boiling in a variable-bypass vaporizer", "To prevent crystallization of Desflurane crystals in cold operating rooms", "To liquefy pipeline nitrous oxide carrier gas"],
        "correct_index": 1,
        "explanation": "Because Desflurane boils at 22.8°C (near room temperature), ambient fluctuations would cause unpredictable boiling and massive agent surges in a conventional variable-bypass vaporizer. The Tec 6 heats it to 39°C (generating a stable vapor pressure of ~2 atm) and injects pure vapor directly into fresh gas flow.",
        "key_points": [
            "Boiling point of Desflurane: 22.8°C; saturated vapor pressure: 669 mmHg at 20°C.",
            "Heated to 39°C to create ~1500 mmHg vapor pressure.",
            "Requires electrical power; has an internal battery alarm for power loss."
        ],
        "sample_viva_answer": "Desflurane boils at 22.8°C, which is near operating room temperature. The Tec 6 vaporizer heats and pressurizes Desflurane to 39°C and 2 atmospheres, turning it into a pressurized vapor that is metered into fresh gas through an electronically controlled valve."
    },
    {
        "id": "AT-EI-04",
        "specialty": "Anaesthesia Technology",
        "topic": "Anaesthesia equipment identification",
        "difficulty": "Beginner",
        "question": "What key anatomical feature differentiates the LMA ProSeal from the first-generation LMA Classic?",
        "options": ["A metal reinforced spiral wire along the entire airway tube", "A dedicated gastric drainage channel that separates the alimentary tract from the respiratory tract", "A built-in video camera at the distal mask tip", "An integrated endotracheal tube cuff manometer"],
        "correct_index": 1,
        "explanation": "The LMA ProSeal features a posterior gastric drain tube parallel to the airway tube. This allows decompression of gastric air, placement of an orogastric tube, venting of accidental regurgitation away from the larynx, and provides a higher seal pressure (up to 30 cmH2O).",
        "key_points": [
            "Gastric drain channel vents stomach contents and enables orogastric tube insertion.",
            "Higher mucosal seal pressure (~30 cmH2O vs ~20 cmH2O in Classic).",
            "Includes a built-in bite block to protect the airway tube."
        ],
        "sample_viva_answer": "The LMA ProSeal includes a second lumen known as the gastric drainage channel. This channel isolates the gastrointestinal tract, allowing gastric decompression via a suction tube and venting regurgitated fluid away from the glottis."
    },
    {
        "id": "AT-EI-05",
        "specialty": "Anaesthesia Technology",
        "topic": "Anaesthesia equipment identification",
        "difficulty": "Intermediate",
        "question": "Where should the tip of a curved Macintosh laryngoscope blade be placed during direct laryngoscopy?",
        "options": ["Directly posterior to the vocal cords", "Into the vallecula (the fold between base of tongue and epiglottis) to indirectly lift the epiglottis by tensioning the glossoepiglottic ligament", "Directly underneath the epiglottis to scoop it upwards directly", "Inside the pyriform fossa"],
        "correct_index": 1,
        "explanation": "The curved Macintosh blade is inserted into the vallecula. Forward and upward lift along the axis of the handle tensions the median glossoepiglottic ligament, indirectly elevating the epiglottis to expose the laryngeal inlet without touching the sensitive laryngeal surface of the epiglottis.",
        "key_points": [
            "Macintosh (curved): tip enters vallecula; indirect epiglottic lift.",
            "Miller (straight): passes posterior to epiglottis; lifts epiglottis directly.",
            "Straight Miller blade is preferred in neonates and infants due to a floppy, U-shaped epiglottis."
        ],
        "sample_viva_answer": "The tip of a curved Macintosh blade is placed into the vallecula, anterior to the epiglottis. Upward traction on the glossoepiglottic fold elevates the epiglottis indirectly to visualize the glottic opening."
    },
    {
        "id": "AT-EI-06",
        "specialty": "Anaesthesia Technology",
        "topic": "Anaesthesia equipment identification",
        "difficulty": "Intermediate",
        "question": "What is the primary clinical advantage of a hyperangulated videolaryngoscope blade (e.g., GlideScope) over a standard Macintosh direct laryngoscope blade?",
        "options": ["Eliminates the requirement for a rigid stylet", "Provides a clear indirect view of the glottis without requiring direct line-of-sight alignment of oral, pharyngeal, and laryngeal axes", "Eliminates the need for pre-oxygenation", "Automatically inflates the endotracheal tube cuff"],
        "correct_index": 1,
        "explanation": "Direct laryngoscopy requires physical line-of-sight alignment of the three anatomical axes (oral, pharyngeal, laryngeal). Hyperangulated videolaryngoscope blades look around the corner with a camera at the blade tip (60° angle), visualizing the cords without requiring neck hyperextension or axis alignment.",
        "key_points": [
            "Visualizes glottis without direct line-of-sight alignment.",
            "Crucial for cervical spine immobility, limited mouth opening, or morbid obesity.",
            "Requires a pre-shaped rigid stylet matching the 60° blade curve to deliver the tube."
        ],
        "sample_viva_answer": "A hyperangulated videolaryngoscope provides an indirect video image of the glottic opening without requiring line-of-sight alignment of the airway axes, making it highly effective in patients with difficult airways or restricted cervical spine mobility."
    },
    {
        "id": "AT-EI-07",
        "specialty": "Anaesthesia Technology",
        "topic": "Anaesthesia equipment identification",
        "difficulty": "Beginner",
        "question": "What is the primary clinical use of Magill forceps in anaesthesia practice?",
        "options": ["To clamp the high-pressure oxygen pipeline hose", "To guide an endotracheal tube into the laryngeal inlet during nasotracheal intubation and extract pharyngeal foreign bodies under direct vision", "To hold surgical skin flaps during tracheostomy", "To dilate the cricothyroid membrane during cricothyroidotomy"],
        "correct_index": 1,
        "explanation": "Magill forceps are angled forceps designed so that the user's hand remains out of the line of sight during laryngoscopy. They are primarily used to grasp and guide the tip of an endotracheal tube into the glottis during nasotracheal intubation, or to place throat packs and remove foreign bodies.",
        "key_points": [
            "Angled design keeps examiner's hand out of the line of vision.",
            "Serrated circular tips securely grasp ETT without puncturing cuff.",
            "Used for nasotracheal tube guidance, nasogastric tube passage, and foreign body removal."
        ],
        "sample_viva_answer": "Magill forceps have a specialized double-angled design that keeps the operator's fingers outside the field of view. They are used under direct laryngoscopy to steer an endotracheal tube into the trachea during nasal intubation."
    },
    {
        "id": "AT-EI-08",
        "specialty": "Anaesthesia Technology",
        "topic": "Anaesthesia equipment identification",
        "difficulty": "Intermediate",
        "question": "During a difficult intubation using a Gum Elastic Bougie (Eschmann Tracheal Tube Introducer), what tactile sensation confirms correct tracheal placement rather than esophageal insertion?",
        "options": ["A smooth, resistance-free passage past 40 cm without any tactile feedback", "Distinct tactile vibrations ('clicks') as the coudé tip rubs against anterior cartilaginous tracheal rings, followed by 'hold-up' at 25-35 cm at the carina", "A sudden pneumatic whistling sound from the lumen", "Immediate spontaneous inflation of the pilot balloon"],
        "correct_index": 1,
        "explanation": "The bougie has an angled (coudé) tip. In the trachea, the operator feels characteristic 'clicks' as the tip bumps against anterior cartilaginous tracheal rings. Advancing further produces definitive 'hold-up' at 25-35 cm as it wedges into a mainstem bronchus. The esophagus has no rings and offers no hold-up (passing endlessly into stomach).",
        "key_points": [
            "Tactile 'clicks' over tracheal rings confirm airway entry.",
            "'Hold-up' at ~25-35 cm at carina or mainstem bronchus confirms tracheal placement.",
            "In esophagus, passes smoothly to 50+ cm without clicks or hold-up."
        ],
        "sample_viva_answer": "Tracheal entry of a bougie is confirmed tactically by 'tracheal clicks' as the angled coudé tip glides across the cartilaginous tracheal rings, followed by definitive 'hold-up' at approximately 25 to 35 cm when it reaches the bronchial tree."
    },
    {
        "id": "AT-EI-09",
        "specialty": "Anaesthesia Technology",
        "topic": "Anaesthesia equipment identification",
        "difficulty": "Advanced",
        "question": "According to the Mapleson classification of breathing circuits, which circuit is the most efficient for spontaneous breathing (requiring fresh gas flow equal to alveolar ventilation)?",
        "options": ["Mapleson A (Magill attachment)", "Mapleson B", "Mapleson D (Bain circuit)", "Mapleson E (Ayre's T-piece)"],
        "correct_index": 0,
        "explanation": "For spontaneous breathing, Mapleson A is the most efficient (requiring fresh gas flow equal to minute ventilation, ~0.8-1.0 x Ve). For controlled (mechanical) ventilation, Mapleson D is the most efficient (Mnemonic for spontaneous: 'All Dogs Bite Canines' = A > D > B > C).",
        "key_points": [
            "Spontaneous breathing efficiency: A > D > B > C.",
            "Controlled mechanical ventilation efficiency: D > B > C > A.",
            "Mapleson D (Bain coaxial circuit) is widely used in controlled transport ventilation."
        ],
        "sample_viva_answer": "Mapleson A is the most efficient circuit for spontaneous breathing because fresh gas flow flushes expired dead space gas through the APL valve near the patient, requiring fresh gas flow roughly equal to resting minute ventilation."
    },
    {
        "id": "AT-EI-10",
        "specialty": "Anaesthesia Technology",
        "topic": "Anaesthesia equipment identification",
        "difficulty": "Intermediate",
        "question": "In an active Waste Anaesthetic Gas Scavenging (WAGS) system interface, what is the role of positive and negative pressure relief valves?",
        "options": ["To calibrate volatile agent vaporizers", "To prevent transmission of positive pressure (circuit barotrauma) or negative suction pressure (circuit emptying and pulmonary edema) to the patient breathing circuit", "To pressurize pipeline oxygen to 50 psi", "To filter carbon dioxide out of exhaled volatile gases"],
        "correct_index": 1,
        "explanation": "Active scavenging connects to hospital vacuum. The interface contains a reservoir bag, a positive pressure relief valve (opens if disposal is occluded to prevent barotrauma), and a negative pressure relief valve (draws in ambient air if vacuum suction is excessive, preventing collapse of the breathing bag and sub-atmospheric pulmonary edema).",
        "key_points": [
            "Positive pressure relief valve: prevents barotrauma if scavenger vents clog.",
            "Negative pressure relief valve: prevents hospital suction from pulling gas from patient lungs.",
            "Active scavenging uses dedicated vacuum; passive relies on patient exhalation pressure."
        ],
        "sample_viva_answer": "The relief valves in an active scavenging interface protect the breathing system: the positive relief valve prevents circuit barotrauma if disposal is blocked, while the negative relief valve entrains room air to prevent vacuum from siphoning gas from the patient circuit."
    },
    {
        "id": "AT-EI-11",
        "specialty": "Anaesthesia Technology",
        "topic": "Anaesthesia equipment identification",
        "difficulty": "Advanced",
        "question": "What is the primary indication for using a Double-Lumen Endobronchial Tube (DLT, such as a Left-sided Robertshaw) in thoracic surgery?",
        "options": ["To provide high-frequency jet ventilation to both lungs simultaneously", "To achieve anatomical lung separation and permit independent one-lung ventilation while operating on the ipsilateral lung", "To administer nebulized surfactant directly into the trachea", "To bypass upper airway trauma without endotracheal intubation"],
        "correct_index": 1,
        "explanation": "A DLT has two distinct lumens and two cuffs (a clear high-volume/low-pressure tracheal cuff and a blue low-volume/high-pressure bronchial cuff). It provides lung isolation, allowing one lung to be collapsed during thoracic surgery while ventilating the dependent lung, or protecting a healthy lung from contamination (pus/blood).",
        "key_points": [
            "Left-sided DLT is used in the majority of cases because the left main bronchus is longer (~5 cm vs ~1.5-2 cm on right).",
            "Right DLT has a specialized slotted bronchial cuff to ventilate the right upper lobe bronchus.",
            "Correct placement is verified with a flexible pediatric bronchoscope."
        ],
        "sample_viva_answer": "A double-lumen endobronchial tube is indicated for anatomical and physiological lung isolation. It allows non-dependent lung deflation during thoracic surgery to facilitate surgical exposure while providing safe mechanical ventilation to the dependent lung."
    },
    {
        "id": "AT-EI-12",
        "specialty": "Anaesthesia Technology",
        "topic": "Anaesthesia equipment identification",
        "difficulty": "Intermediate",
        "question": "What bedside safety check is performed using Pethick's test on a Bain coaxial breathing circuit?",
        "options": ["Measures the concentration of sevoflurane in the bag", "Verifies the physical integrity and patency of the inner fresh gas delivery tube to ensure it is not disconnected, kinked, or cracked", "Calibrates the APL valve to 70 cmH2O", "Tests the battery backup of the workstation ventilator"],
        "correct_index": 1,
        "explanation": "In a Bain coaxial circuit, fresh gas flows through an inner narrow tube surrounded by an outer corrugated expiratory tube. If the inner tube disconnects or cracks at the machine end, the entire circuit becomes dead space, causing severe hypercapnia. Pethick's test occludes the inner tube at the patient end using a finger while pressing the O2 flush to verify that the reservoir bag deflates via the Venturi effect.",
        "key_points": [
            "Bain circuit: coaxial design (inner tube = fresh gas; outer tube = exhaled gas).",
            "Pethick's test verifies inner tube is intact and patent.",
            "Bag flattens during O2 flush with inner tube occluded due to Venturi entrainment."
        ],
        "sample_viva_answer": "Pethick's test verifies the integrity of the inner fresh gas delivery tube in a coaxial Bain circuit. By occluding the inner tube and activating the oxygen flush, the reservoir bag flattens due to the Venturi effect, proving the inner tube is intact and connected."
    }
]

AT_MC_QUESTIONS = [
    {
        "id": "AT-MC-01",
        "specialty": "Anaesthesia Technology",
        "topic": "Basic machine components",
        "difficulty": "Beginner",
        "question": "What is the primary function of the Oxygen Flush (O2 Flush) valve on an anaesthesia workstation?",
        "options": ["Delivers vaporized volatile agent at maximum dial concentration", "Delivers 100% pure oxygen directly from the pipeline or cylinder pressure regulator bypassing the flowmeters and vaporizers at 35 to 75 L/min", "Calibrates the paramagnetic oxygen sensor", "Flushes carbon dioxide into the scavenging canister"],
        "correct_index": 1,
        "explanation": "The O2 flush valve delivers unmetered, pure oxygen directly to the common gas outlet at a high flow rate of 35 to 75 L/min at 45 to 55 psi, bypassing the rotameter flowmeters and vaporizers. It must never be pressed during the inspiratory phase of mechanical ventilation due to the severe risk of barotrauma.",
        "key_points": [
            "Delivers 35-75 L/min of 100% O2 directly to common gas outlet.",
            "Bypasses flowmeters and volatile vaporizers.",
            "Risk of barotrauma and patient awareness if activated during inspiration."
        ],
        "sample_viva_answer": "The oxygen flush valve delivers 100% oxygen at 35-75 L/min directly from the high/intermediate pressure circuit to the common gas outlet, bypassing flowmeters and vaporizers. It should never be activated during inspiration to avoid barotrauma."
    },
    {
        "id": "AT-MC-02",
        "specialty": "Anaesthesia Technology",
        "topic": "Basic machine components",
        "difficulty": "Intermediate",
        "question": "What is the purpose of the Adjustable Pressure Limiting (APL) or 'pop-off' valve during manual bag-mask ventilation?",
        "options": ["To measure volatile agent vapor pressure", "To adjust circuit pressure and vent excess fresh gas into the waste scavenging system", "To connect the vacuum pipeline to the endotracheal tube", "To calibrate the spirometry flow sensor"],
        "correct_index": 1,
        "explanation": "The APL valve allows the anaesthesia provider to adjust circuit pressure during spontaneous or manual bag ventilation. Clockwise rotation increases circuit pressure for bagging, while counter-clockwise rotation vents excess gas into the scavenger, preventing lung overdistension.",
        "key_points": [
            "Fully open during spontaneous breathing to prevent high resistance.",
            "Partially closed during manual bag ventilation to generate positive pressure.",
            "Must be isolated/bypassed when switching to mechanical ventilator mode."
        ],
        "sample_viva_answer": "The APL valve controls circuit pressure during manual or spontaneous breathing by venting excess gas into the scavenging system. It is opened for spontaneous breathing and adjusted to generate adequate tidal volumes during manual bagging."
    },
    {
        "id": "AT-MC-03",
        "specialty": "Anaesthesia Technology",
        "topic": "Basic machine components",
        "difficulty": "Beginner",
        "question": "When reading a mechanical rotameter gas flowmeter, where is the flow rate reading taken for a ball float versus a bobbin (skirted float)?",
        "options": ["Always at the bottom for both", "At the center/equator for a ball float; at the top surface for a bobbin float", "At the bottom of a ball float; at the center of a bobbin float", "At the top of the glass tube regardless of float position"],
        "correct_index": 1,
        "explanation": "In variable-orifice rotameters, spherical ball floats are read across their widest center equator point. Cylindrical or skirted bobbin floats with rotating flutes are read across their top horizontal rim.",
        "key_points": [
            "Ball float: read at the middle/equator.",
            "Bobbin/skirted float: read at the top flat surface.",
            "Flutes on bobbins cause them to spin, confirming the float is not stuck against the tube wall."
        ],
        "sample_viva_answer": "A ball float is read across its center equator, whereas a bobbin or skirted float is read at the top edge of its upper rim."
    },
    {
        "id": "AT-MC-04",
        "specialty": "Anaesthesia Technology",
        "topic": "Basic machine components",
        "difficulty": "Intermediate",
        "question": "What is the standardized outside/inside diameter dimension of the Common Gas Outlet (CGO) on an anaesthesia machine?",
        "options": ["10 mm female / 14 mm male", "15 mm internal female / 22 mm external male conical connector", "30 mm female / 35 mm male", "50 mm threaded screw connector"],
        "correct_index": 1,
        "explanation": "The common gas outlet conforms to international ISO standards with an outer diameter of 22 mm male and an inner diameter of 15 mm female conical taper. This matches standard breathing circuit connections and resuscitation masks.",
        "key_points": [
            "ISO standard: 15 mm female / 22 mm male connector.",
            "Common gas outlet receives mixed fresh gas from flowmeters and vaporizers.",
            "Some machines have an Auxiliary CGO (ACGO) switch to feed Mapleson circuits."
        ],
        "sample_viva_answer": "The common gas outlet has a standardized conical connection: 15 mm internal female diameter and 22 mm external male diameter, ensuring universal compatibility with standard breathing circuits."
    },
    {
        "id": "AT-MC-05",
        "specialty": "Anaesthesia Technology",
        "topic": "Basic machine components",
        "difficulty": "Advanced",
        "question": "Why is the oxygen flowmeter tube always placed in the most downstream (furthest right in the US/UK manifold) position in a multi-gas flowmeter block?",
        "options": ["Because oxygen gas is lighter than air and nitrous oxide", "To minimize the risk of delivering a hypoxic gas mixture to the patient if a leak or crack develops in any upstream flowmeter tube", "Because oxygen pipeline pressure is higher than nitrous oxide", "To make it easier for left-handed anaesthesiologists to reach"],
        "correct_index": 1,
        "explanation": "If oxygen were upstream of nitrous oxide or air, a crack or leak in any downstream flowmeter tube would allow oxygen to escape into the room while nitrous oxide continued to the common gas outlet, creating a lethal hypoxic mixture. Placing oxygen furthest downstream ensures that in a leak, non-oxygen gases escape first.",
        "key_points": [
            "Oxygen flowmeter is always downstream (rightmost).",
            "Protects patient from hypoxic gas mixtures during tube leaks.",
            "Universal design requirement in international safety standards (ASTM/ISO)."
        ],
        "sample_viva_answer": "Oxygen is placed downstream of all other gas flowmeters so that if any leak or crack develops in upstream glass tubes, nitrous oxide or air leaks out into the room rather than oxygen, preventing the delivery of a hypoxic gas mixture."
    },
    {
        "id": "AT-MC-06",
        "specialty": "Anaesthesia Technology",
        "topic": "Basic machine components",
        "difficulty": "Intermediate",
        "question": "What is the function of the vaporizer interlocking (Selectatec) manifold system?",
        "options": ["To lock the vaporizer dial permanently at 2%", "To mechanically ensure that only one volatile agent vaporizer can be turned on at any given time, preventing accidental cross-mixing of agents", "To automatically refill empty vaporizers from pipeline canisters", "To electronically heat both vaporizers simultaneously"],
        "correct_index": 1,
        "explanation": "The Selectatec interlock system uses interlocking sliding pins. Turning the dial of one vaporizer extends locking pins that physically block the control knobs of adjacent vaporizers, ensuring only one anesthetic agent can be turned on at a time.",
        "key_points": [
            "Prevents simultaneous delivery of two volatile anesthetic agents.",
            "Prevents cross-contamination of liquid agents inside adjacent vaporizers.",
            "Isolated vaporizers are locked out of the fresh gas stream."
        ],
        "sample_viva_answer": "The vaporizer interlock system mechanically locks adjacent vaporizers so that only one vaporizer can be turned on at a time. This prevents simultaneous administration of multiple volatile agents and cross-contamination."
    },
    {
        "id": "AT-MC-07",
        "specialty": "Anaesthesia Technology",
        "topic": "Basic machine components",
        "difficulty": "Advanced",
        "question": "Which of the following components belongs to the High-Pressure circuit of an anaesthesia machine?",
        "options": ["Rotameter flowmeter glass tubes", "Hanger yoke assembly, yoke block check valve, and cylinder pressure gauge/regulator", "Vaporizer bypass manifold", "Common gas outlet"],
        "correct_index": 1,
        "explanation": "The high-pressure system includes all components upstream of cylinder pressure regulators (pressures up to 2200 psi for O2 cylinders): cylinder yokes, index pins, check valves, and cylinder pressure indicators. The intermediate system is pipeline pressure (~50 psi). The low-pressure system is downstream of flow control valves.",
        "key_points": [
            "High pressure: cylinder yokes, cylinders, cylinder gauges (up to 2200 psi).",
            "Intermediate pressure: pipeline inlets, O2 flush valve, fail-safe valves (45-55 psi).",
            "Low pressure: flowmeters, vaporizers, common gas outlet (near atmospheric pressure)."
        ],
        "sample_viva_answer": "The high-pressure system includes the cylinder hanger yokes, cylinder pressure gauges, and the primary pressure regulators. It receives high pressures from compressed gas cylinders up to 2200 psi."
    },
    {
        "id": "AT-MC-08",
        "specialty": "Anaesthesia Technology",
        "topic": "Basic machine components",
        "difficulty": "Beginner",
        "question": "Why are 'ascending' (hanging bellows) ventilators considered much safer than 'descending' bellows ventilators on modern anaesthesia machines?",
        "options": ["Ascending bellows require no driving gas", "An ascending bellows ascends during exhalation and will collapse and fail to fill if a circuit disconnection occurs, immediately alarming the clinician", "Ascending bellows are completely silent", "Ascending bellows generate negative end-expiratory pressure"],
        "correct_index": 1,
        "explanation": "Ascending bellows rise during exhalation (as expired gas fills them) and drop during inspiration. If a breathing circuit disconnects, expired gas is lost; gravity causes the ascending bellows to collapse flat, providing immediate visual and alarm confirmation of disconnection. In contrast, descending bellows drop by gravity and can continue moving even when disconnected, drawing in room air.",
        "key_points": [
            "Ascending bellows: rise on expiration; fall on inspiration. Collapse on disconnect.",
            "Descending bellows: fall on expiration by gravity; can mask disconnects by drawing room air.",
            "Ascending bellows design is mandated by safety standards."
        ],
        "sample_viva_answer": "Ascending bellows are safer because they rise during exhalation and drop during inspiration. In the event of a circuit disconnection, the bellows collapses to the bottom of the canister and fails to rise, providing immediate visual confirmation of a leak or disconnect."
    },
    {
        "id": "AT-MC-09",
        "specialty": "Anaesthesia Technology",
        "topic": "Basic machine components",
        "difficulty": "Intermediate",
        "question": "What is the purpose of the unidirectional check valves (inspiratory and expiratory valves) inside the circle breathing system?",
        "options": ["To pressurize the vaporizer liquid chamber", "To ensure gas flows in a continuous one-way loop (inspiratory limb to patient, expiratory limb to absorber) and prevent rebreathing of carbon dioxide before absorption", "To prevent room air from entering the scavenging vacuum", "To humidify inspired medical gases"],
        "correct_index": 1,
        "explanation": "The unidirectional valves contain lightweight discs that rise and fall with breathing efforts. They ensure that fresh gas and rebreathed gas flow exclusively in one direction through the circle system, preventing exhaled CO2 from entering the inspiratory limb before passing through the absorber.",
        "key_points": [
            "Ensure unidirectional circular flow through the breathing circuit.",
            "Condensation or moisture can cause the valve disc to stick open or closed.",
            "An incompetent (stuck open) valve allows bidirectional gas flow and massive CO2 rebreathing."
        ],
        "sample_viva_answer": "Unidirectional valves ensure one-way flow of gas through the circle system: inspiratory gas flows toward the patient, and exhaled gas travels through the expiratory limb to the CO2 absorber, preventing rebreathing of unabsorbed exhaled carbon dioxide."
    },
    {
        "id": "AT-MC-10",
        "specialty": "Anaesthesia Technology",
        "topic": "Basic machine components",
        "difficulty": "Beginner",
        "question": "What does the primary cylinder pressure regulator do on an anaesthesia machine?",
        "options": ["Heats the cylinder to prevent freezing", "Reduces high and variable cylinder pressure (~2000 psi for O2) down to a constant intermediate operating pressure of approximately 45 to 50 psi", "Increases pipeline gas pressure to 100 psi", "Filters carbon monoxide out of cylinder gas"],
        "correct_index": 1,
        "explanation": "The primary pressure regulator reduces cylinder pressure from up to 2200 psi down to a safe, constant operating pressure of 45-50 psi. This protects machine components and ensures smooth, consistent gas delivery identical to pipeline sources.",
        "key_points": [
            "Reduces ~2000 psi cylinder pressure to 45-50 psi.",
            "Regulator pressure is set slightly lower than pipeline pressure (~50-55 psi) so pipeline gas is consumed preferentially when cylinders are open.",
            "Prevents pressure fluctuations as the cylinder empties."
        ],
        "sample_viva_answer": "The cylinder pressure regulator reduces high, fluctuating cylinder pressure from around 2000 psi down to a constant intermediate pressure of 45 to 50 psi, protecting the machine circuit and ensuring steady gas flow."
    },
    {
        "id": "AT-MC-11",
        "specialty": "Anaesthesia Technology",
        "topic": "Basic machine components",
        "difficulty": "Advanced",
        "question": "What is the mechanical function of the Hypoxic Guard system (e.g., Link-25 proportioning system) connecting oxygen and nitrous oxide flow control valves?",
        "options": ["Shuts off all electricity during an oxygen alarm", "Mechanically links the oxygen and nitrous oxide control gears with a bicycle chain or pneumatic system to ensure a minimum delivered oxygen concentration of at least 25%", "Prevents oxygen flow from exceeding 10 L/min", "Vents nitrous oxide into the scavenging system during induction"],
        "correct_index": 1,
        "explanation": "The Link-25 system uses a mechanical gear link (29 teeth for N2O, 14 teeth for O2) connecting the spindle valves. If nitrous oxide is increased such that oxygen would drop below 25%, the gear mechanically forces the oxygen needle valve open to maintain at least 25% FiO2.",
        "key_points": [
            "Enforces a minimum delivered O2 concentration of 25% (in N2O/O2 mixtures).",
            "Mechanically links N2O and O2 flow control knobs.",
            "Does NOT protect against delivery of hypoxic gas if the supply line contains the wrong gas."
        ],
        "sample_viva_answer": "The hypoxic guard or Link-25 system mechanically links the oxygen and nitrous oxide flowmeter spindles via a gear-and-chain mechanism, ensuring that the delivered oxygen concentration never drops below 25%."
    },
    {
        "id": "AT-MC-12",
        "specialty": "Anaesthesia Technology",
        "topic": "Basic machine components",
        "difficulty": "Intermediate",
        "question": "What is the function of the Auxiliary Common Gas Outlet (ACGO) switch found on modern anaesthesia workstations?",
        "options": ["Activates the electrical battery backup mode", "Diverts fresh gas flow away from the internal circle system to an external port used for connecting non-circle circuits (e.g., Bain or Jackson-Rees circuit)", "Opens the drain port of the water condensation trap", "Calibrates the inspiratory pressure transducer"],
        "correct_index": 1,
        "explanation": "The ACGO switch allows the operator to divert fresh gas output from the internal breathing circle system to a dedicated external nipple outlet, enabling the use of non-rebreathing Mapleson pediatric circuits or transport breathing assemblies.",
        "key_points": [
            "Diverts fresh gas from circle system to external auxiliary outlet.",
            "Used for Mapleson D (Bain) or Mapleson F (Jackson-Rees) pediatric circuits.",
            "Safety interlock: internal workstation ventilator cannot ventilate when ACGO is active."
        ],
        "sample_viva_answer": "The ACGO switch directs fresh gas flow away from the internal circle system to an external port, allowing the anaesthetist to connect external breathing circuits like a Bain circuit or Jackson-Rees circuit for pediatric cases."
    }
]

# =========================================================================
# ANAESTHESIA TECHNOLOGY: Safety Checks & Monitoring (24 questions)
# =========================================================================

AT_SC_QUESTIONS = [
    {
        "id": "AT-SC-01",
        "specialty": "Anaesthesia Technology",
        "topic": "Equipment safety checks",
        "difficulty": "Intermediate",
        "question": "Which safety system prevents incorrect cross-connection between high-pressure medical gas cylinders and the anaesthesia machine yoke hanger?",
        "options": ["Diameter Index Safety System (DISS)", "Pin Index Safety System (PISS)", "Quick-Connect Schrader Coupler", "Pressure-Relief Pop-off Valve"],
        "correct_index": 1,
        "explanation": "The Pin Index Safety System (PISS) uses specific physical pin and hole configurations on cylinder valves and yoke hanger assemblies to mechanically prevent the connection of an incorrect gas cylinder (e.g., Oxygen is pin positions 2 and 5, Nitrous Oxide is 3 and 5).",
        "key_points": [
            "PISS applies to high-pressure small cylinders (Sizes A through E).",
            "DISS applies to pipeline hose connections (diameter and thread variations).",
            "Oxygen pin position: 2 and 5; Air: 1 and 5; Nitrous oxide: 3 and 5."
        ],
        "sample_viva_answer": "The Pin Index Safety System (PISS) uses unique pin locations on cylinder yokes to physically prevent mounting the wrong gas cylinder onto an anaesthesia machine hanger yoke. Oxygen uses pins 2 and 5."
    },
    {
        "id": "AT-SC-02",
        "specialty": "Anaesthesia Technology",
        "topic": "Equipment safety checks",
        "difficulty": "Advanced",
        "question": "What does the oxygen fail-safe mechanism (pressure-sensor shut-off valve) inside an anaesthesia machine do when oxygen supply pressure drops below 30 psi?",
        "options": ["Automatically increases vaporizer concentration to compensate", "Shuts off or proportionately reduces the flow of nitrous oxide and other non-oxygen gases", "Triggers electric defibrillation alarms", "Switches the ventilator to ambient air suction"],
        "correct_index": 1,
        "explanation": "The fail-safe valve ensures that if the supply pressure of oxygen drops below approximately 30 psi, the flow of nitrous oxide and other gases is proportionately reduced or completely cut off to prevent the delivery of a hypoxic gas mixture to the patient.",
        "key_points": [
            "Protects against delivery of hypoxic gas mixtures during oxygen pipeline or cylinder failure.",
            "Nitrous oxide cutoff occurs before complete oxygen exhaustion.",
            "Does NOT detect cross-contamination or hypoxic gas inside the oxygen line itself—that requires an FiO2 analyzer."
        ],
        "sample_viva_answer": "The fail-safe valve detects a decline in oxygen line pressure below ~30 psi and cuts off or throttles nitrous oxide flow, protecting the patient from receiving a hypoxic gas mixture."
    },
    {
        "id": "AT-SC-03",
        "specialty": "Anaesthesia Technology",
        "topic": "Equipment safety checks",
        "difficulty": "Beginner",
        "question": "What pin positions on the Pin Index Safety System (PISS) yoke correspond to medical Oxygen and medical Nitrous Oxide cylinders, respectively?",
        "options": ["Oxygen: 1, 5; Nitrous Oxide: 2, 5", "Oxygen: 2, 5; Nitrous Oxide: 3, 5", "Oxygen: 3, 5; Nitrous Oxide: 1, 5", "Oxygen: 2, 4; Nitrous Oxide: 1, 6"],
        "correct_index": 1,
        "explanation": "Under PISS standards, pins are arranged along a 7-position circular arc: Oxygen uses positions 2 and 5; Nitrous Oxide uses 3 and 5; Medical Air uses 1 and 5; Entonox (50% O2 / 50% N2O) uses 7.",
        "key_points": [
            "Oxygen: pins 2 and 5.",
            "Nitrous oxide: pins 3 and 5.",
            "Air: pins 1 and 5."
        ],
        "sample_viva_answer": "In the Pin Index Safety System, oxygen cylinders utilize pin positions 2 and 5, while nitrous oxide cylinders use pin positions 3 and 5."
    },
    {
        "id": "AT-SC-04",
        "specialty": "Anaesthesia Technology",
        "topic": "Equipment safety checks",
        "difficulty": "Intermediate",
        "question": "What does the Diameter Index Safety System (DISS) regulate in an operating theatre setting?",
        "options": ["The diameter of endotracheal tube connectors", "The threaded diameter and collar dimensions of pipeline gas supply hoses and wall inlet station couplers to prevent gas line interchange", "The size of volatile agent filler spouts", "The suction catheter lumen diameter"],
        "correct_index": 1,
        "explanation": "DISS governs non-interchangeable, gas-specific threaded connections on pipeline hoses (operating at 50 psi) and machine wall inlets. Each gas fitting has unique internal and external diameters and thread pitches, preventing cross-connection of pipeline gas hoses.",
        "key_points": [
            "Applies to intermediate-pressure pipeline connections (50 psi).",
            "Each gas fitting has distinct collar diameter and thread pitch.",
            "Prevents connecting an oxygen hose to a nitrous oxide or air wall outlet."
        ],
        "sample_viva_answer": "The Diameter Index Safety System (DISS) uses gas-specific diameters and threaded couplings for pipeline hoses and station outlets to physically prevent connecting the wrong pipeline gas hose into an anaesthesia machine."
    },
    {
        "id": "AT-SC-05",
        "specialty": "Anaesthesia Technology",
        "topic": "Equipment safety checks",
        "difficulty": "Advanced",
        "question": "How is a Universal Negative Pressure Leak Check performed on the low-pressure circuit of an anaesthesia workstation?",
        "options": ["By blowing compressed air into the breathing circuit at 40 cmH2O", "By attaching a suction bulb to the common gas outlet with machine master switch OFF and vaporizers opened, squeezing the bulb flat, and observing if it stays collapsed for at least 10 seconds", "By immersing the flowmeters in soapy water", "By monitoring the battery voltage during power cycling"],
        "correct_index": 1,
        "explanation": "The 1993 FDA pre-use checkout protocol uses a negative pressure bulb attached to the machine's common gas outlet. With the machine master switch off and vaporizers turned on individually, the bulb is squeezed flat. A leak is present if the bulb re-inflates in under 10 seconds (detects leaks as small as 30 mL/min).",
        "key_points": [
            "Tests the low-pressure system (downstream of flow control valves to common gas outlet).",
            "Tests vaporizers for internal and mounting seal leaks.",
            "Bulb must remain collapsed for >= 10 seconds."
        ],
        "sample_viva_answer": "A negative pressure leak test uses a suction bulb attached to the common gas outlet. With machine off and each vaporizer turned on, the collapsed bulb must remain completely flat for at least 10 seconds, proving the absence of low-pressure circuit leaks."
    },
    {
        "id": "AT-SC-06",
        "specialty": "Anaesthesia Technology",
        "topic": "Equipment safety checks",
        "difficulty": "Beginner",
        "question": "During the daily pre-use checkout of the oxygen analyzer, what two oxygen concentrations must be used for sensor calibration?",
        "options": ["0% and 50%", "21% (room air) and 100% pure oxygen (using the oxygen flush)", "50% and 100%", "21% and 40%"],
        "correct_index": 1,
        "explanation": "Standard 2-point calibration of an oxygen analyzer requires calibrating the baseline against ambient room air (21% O2), followed by exposure to 100% oxygen (via oxygen flush or 100% O2 flow). The reading must stabilize at 21% (+/- 2%) and 100% (+/- 2%).",
        "key_points": [
            "Two-point calibration: Room Air (21%) and Pure Oxygen (100%).",
            "Verifies linearity and response time of galvanic or paramagnetic sensor.",
            "Crucial safety device: the ONLY monitor that detects pipeline hypoxic gas crossover."
        ],
        "sample_viva_answer": "The oxygen analyzer must be calibrated at two points: exposed first to room air to read 21%, and then exposed to pure oxygen via the O2 flush to verify a reading of 100%."
    },
    {
        "id": "AT-SC-07",
        "specialty": "Anaesthesia Technology",
        "topic": "Equipment safety checks",
        "difficulty": "Intermediate",
        "question": "How is the Positive Pressure Leak Test performed on a circle breathing system prior to induction?",
        "options": ["Open the APL valve completely and run 10 L/min of O2", "Occlude the patient Y-piece, close the APL valve to 30 to 40 cmH2O, pressurize the circuit to 30 cmH2O with O2 flush, and verify circuit pressure holds steady for at least 10 seconds", "Disconnect the expiratory limb and check for water condensation", "Press the emergency silence button for 15 seconds"],
        "correct_index": 1,
        "explanation": "To test the circle system for leaks, the Y-piece is occluded, the APL valve is fully closed, and the system is pressurized to 30 cmH2O using the O2 flush. The pressure gauge should hold steady for at least 10 seconds without dropping, demonstrating that the hoses, absorber, and valves are airtight.",
        "key_points": [
            "Tests breathing circuit, canister, and bag mount for leaks.",
            "Pressurize to 30 cmH2O and hold for 10 seconds.",
            "Next step: open APL valve to confirm pressure releases into scavenger."
        ],
        "sample_viva_answer": "The positive pressure circle test is performed by occluding the Y-piece, closing the APL valve, pressurizing the circuit to 30 cmH2O using the O2 flush, and verifying that the circuit pressure holds without dropping for at least 10 seconds."
    },
    {
        "id": "AT-SC-08",
        "specialty": "Anaesthesia Technology",
        "topic": "Equipment safety checks",
        "difficulty": "Advanced",
        "question": "If an in-line oxygen analyzer alarms at 18% during surgery while ventilating with pipeline oxygen, what is the mandatory immediate emergency management sequence?",
        "options": ["Recalibrate the analyzer and continue", "Immediately disconnect the pipeline oxygen hose from the wall, turn on the backup oxygen E-cylinder, and ventilate manually with the reservoir bag", "Turn on nitrous oxide flow to 10 L/min", "Switch to descending bellows mode"],
        "correct_index": 1,
        "explanation": "A falling FiO2 on pipeline oxygen indicates pipeline contamination or pipeline crossover (e.g., nitrogen or N2O entering the O2 line). Leaving the pipeline connected will override the cylinder regulator (since pipeline pressure is ~50-55 psi while cylinder regulator is ~45 psi). The pipeline MUST be disconnected immediately so the machine draws pure O2 from the cylinder.",
        "key_points": [
            "Disconnect pipeline hose from wall outlet immediately.",
            "Open backup O2 cylinder and ventilate manually.",
            "Never trust pipeline pressure if FiO2 drops; pipeline crossover is a fatal emergency."
        ],
        "sample_viva_answer": "If an oxygen analyzer alarms low on pipeline gas, immediately disconnect the pipeline hose from the wall, open the backup oxygen cylinder, and ventilate manually with the bag. Disconnecting the pipeline is mandatory because pipeline pressure is higher than cylinder regulator pressure and would prevent cylinder flow."
    },
    {
        "id": "AT-SC-09",
        "specialty": "Anaesthesia Technology",
        "topic": "Equipment safety checks",
        "difficulty": "Beginner",
        "question": "What gas-specific quick-connect coupler is commonly used on hospital operating room walls for gas pipelines (e.g., in the UK and Commonwealth countries)?",
        "options": ["Schrader quick-connect couplers with gas-specific probe indexing", "Garden hose thread couplings", "Luer lock twist connectors", "Standard household audio jacks"],
        "correct_index": 0,
        "explanation": "Schrader quick-connect couplers use distinct physical collar diameters and index pins specific to each medical gas (Oxygen, Nitrous Oxide, Medical Air, Vacuum), mechanically preventing insertion of a probe into the wrong terminal wall unit.",
        "key_points": [
            "Gas-specific physical dimensions prevent wrong gas connection.",
            "Spring-loaded internal check valve stops gas escape when disconnected.",
            "Color-coded according to ISO (White = O2) or US standards (Green = O2)."
        ],
        "sample_viva_answer": "Schrader quick-connect couplers use gas-specific probe collars and geometries that only mate with their matching wall socket, mechanically preventing gas line cross-connection."
    },
    {
        "id": "AT-SC-10",
        "specialty": "Anaesthesia Technology",
        "topic": "Equipment safety checks",
        "difficulty": "Intermediate",
        "question": "What toxic substance can be produced when Sevoflurane passes through completely dried/desiccated carbon dioxide absorbent (especially barium hydroxide lime or dry soda lime)?",
        "options": ["Carbon monoxide", "Compound A (fluoromethyl-2,2-difluoro-1-(trifluoromethyl)vinyl ether)", "Phosgene gas", "Nitric oxide"],
        "correct_index": 1,
        "explanation": "Sevoflurane reacts with dry strong bases (potassium hydroxide or sodium hydroxide) in desiccated absorbent to produce Compound A, a haloalkene that causes nephrotoxicity in rat models. Desflurane and isoflurane produce carbon monoxide (CO) with desiccated absorbent.",
        "key_points": [
            "Sevoflurane + desiccated absorbent = Compound A (nephrotoxic risk).",
            "Desflurane / Isoflurane + desiccated absorbent = Carbon Monoxide (CO).",
            "Prevented by maintaining fresh gas flows >= 1-2 L/min and never leaving gas flow on over the weekend."
        ],
        "sample_viva_answer": "Sevoflurane degradation in desiccated carbon dioxide absorbent produces Compound A, which is nephrotoxic in animal models. This is avoided by ensuring absorbents do not become desiccated and using minimum fresh gas flows of 1-2 L/min."
    },
    {
        "id": "AT-SC-11",
        "specialty": "Anaesthesia Technology",
        "topic": "Equipment safety checks",
        "difficulty": "Advanced",
        "question": "Why is it dangerous to leave fresh gas flow running through an anaesthesia workstation over the weekend when the machine is not in use?",
        "options": ["It causes the computer screen to overheat", "Continuous gas flow dries out (desiccates) the carbon dioxide absorbent, creating conditions for carbon monoxide and Compound A production during Monday's cases", "It depletes the central hospital oxygen vacuum liquid reservoir", "It reverses the polarity of the ECG leads"],
        "correct_index": 1,
        "explanation": "Continuous dry gas flow through an idle circle system strips moisture from the soda lime granules. Desiccated absorbent reacts violently with volatile anesthetics (especially Desflurane and Isoflurane) to produce toxic levels of carbon monoxide (CO), causing carboxyhemoglobinemia in subsequent patients.",
        "key_points": [
            "Dries out soda lime moisture content (< 10% water).",
            "Exposes patients to fatal carbon monoxide poisoning upon anesthetic induction.",
            "All fresh gas flows and master power switches must be turned off when not in use."
        ],
        "sample_viva_answer": "Leaving gas flow running desiccates the soda lime. Completely dry absorbent reacts with volatile anesthetics—particularly desflurane—to generate dangerous quantities of carbon monoxide, risking fatal carboxyhemoglobinemia in the next patient."
    },
    {
        "id": "AT-SC-12",
        "specialty": "Anaesthesia Technology",
        "topic": "Equipment safety checks",
        "difficulty": "Beginner",
        "question": "How can an anaesthesia technologist verify that an active waste anaesthetic gas scavenging (WAGS) system is drawing adequate suction without excess negative pressure?",
        "options": ["By smelling the exhaust port", "By inspecting the scavenging flow indicator float, ensuring it hovers between the minimum and maximum indicator marks on the flowmeter tube", "By verifying the breathing bag is sucked completely flat", "By feeling the temperature of the pipeline hose"],
        "correct_index": 1,
        "explanation": "Active scavenging interfaces feature a visual flow indicator (a floating ball or bobbin in a clear tube) or vacuum control valve. The technologist adjusts the needle valve until the float rests within the calibrated green 'normal' zone, confirming sufficient waste removal without excessive vacuum.",
        "key_points": [
            "Float must reside between min and max indicator lines.",
            "Protects operating theatre personnel from exposure to trace anesthetic gases.",
            "Too little vacuum leads to room pollution; excessive vacuum risks subatmospheric circuit pressure."
        ],
        "sample_viva_answer": "The technologist checks the flow indicator float on the scavenging interface, adjusting the suction needle valve until the float rests steadily between the calibrated minimum and maximum marks."
    }
]

AT_MF_QUESTIONS = [
    {
        "id": "AT-MF-01",
        "specialty": "Anaesthesia Technology",
        "topic": "Monitoring fundamentals",
        "difficulty": "Intermediate",
        "question": "On a normal time capnogram, what does Phase III (the alveolar plateau) represent, and what does the end of Phase III (PetCO2) indicate?",
        "options": ["Inspiratory downstroke representing fresh gas flow", "Anatomical dead space emptying free of carbon dioxide", "Exhalation of alveolar gas, with PetCO2 approximating alveolar and arterial CO2 tension", "Rapid filling of the endotracheal tube cuff with room air"],
        "correct_index": 2,
        "explanation": "Phase III represents alveolar gas exhalation. The peak value at the very end of this plateau is the End-Tidal CO2 (PetCO2), which in healthy lungs is typically 2 to 5 mmHg lower than arterial PaCO2 due to normal alveolar dead space.",
        "key_points": [
            "Phase I: Inspiratory baseline (CO2-free anatomical dead space).",
            "Phase II: Expiratory upstroke (mixing of dead space and alveolar gas).",
            "Phase III: Alveolar plateau terminating at PetCO2.",
            "Phase 0: Rapid inspiratory downstroke."
        ],
        "sample_viva_answer": "Phase III is the alveolar plateau representing expired alveolar gas. The highest point at the end of Phase III is PetCO2, which closely estimates arterial PaCO2 in healthy lungs (typically 2-5 mmHg lower)."
    },
    {
        "id": "AT-MF-02",
        "specialty": "Anaesthesia Technology",
        "topic": "Monitoring fundamentals",
        "difficulty": "Beginner",
        "question": "Pulse oximetry estimates arterial oxygen saturation (SpO2) by measuring the differential absorption of which two light wavelengths through pulsating vascular tissue?",
        "options": ["Green (532 nm) and Yellow (589 nm)", "Red (660 nm) and Infrared (940 nm)", "Ultraviolet (340 nm) and Blue (450 nm)", "Radio waves (1 MHz) and Microwave (2.4 GHz)"],
        "correct_index": 1,
        "explanation": "Pulse oximeters emit red light at approximately 660 nm (absorbed predominantly by deoxygenated hemoglobin) and infrared light at approximately 940 nm (absorbed predominantly by oxygenated hemoglobin). The ratio of pulsing absorptions calculates SpO2.",
        "key_points": [
            "Deoxyhemoglobin absorbs more Red light (660 nm).",
            "Oxyhemoglobin absorbs more Infrared light (940 nm).",
            "Carboxyhemoglobin causes falsely elevated readings; Methemoglobin locks reading near 85%."
        ],
        "sample_viva_answer": "Pulse oximetry uses 660 nm (red light) and 940 nm (infrared light). Deoxygenated hemoglobin absorbs more red light, while oxygenated hemoglobin absorbs more infrared light."
    },
    {
        "id": "AT-MF-03",
        "specialty": "Anaesthesia Technology",
        "topic": "Monitoring fundamentals",
        "difficulty": "Intermediate",
        "question": "A sudden, catastrophic drop of End-Tidal CO2 (PetCO2) to zero or near-zero on a ventilated surgical patient most commonly indicates which critical life-threatening events?",
        "options": ["Acute malignant hyperthermia", "Esophageal intubation, complete breathing circuit disconnection, or sudden cardiac arrest / loss of pulmonary blood flow", "Laparoscopic peritoneal insufflation with CO2", "Exhaustion of soda lime granules"],
        "correct_index": 1,
        "explanation": "Carbon dioxide reaches the lungs via pulmonary circulation. A sudden drop of PetCO2 to zero indicates: 1) lack of ventilation (disconnection, extubation, complete airway obstruction); 2) lack of pulmonary perfusion (cardiac arrest, massive pulmonary embolism); or 3) esophageal intubation.",
        "key_points": [
            "Causes of PetCO2 dropping to zero: Disconnection, Cardiac arrest, Esophageal intubation.",
            "Gradual drop: hypothermia, hyperventilation, hypovolemia.",
            "Sudden rise: ROSC during CPR, unclamping of major vessel, malignant hyperthermia."
        ],
        "sample_viva_answer": "A sudden drop of PetCO2 to zero indicates an immediate catastrophe: either a complete loss of circuit connection/ventilation, esophageal intubation, or sudden cardiac arrest with complete cessation of pulmonary blood flow."
    },
    {
        "id": "AT-MF-04",
        "specialty": "Anaesthesia Technology",
        "topic": "Monitoring fundamentals",
        "difficulty": "Advanced",
        "question": "What does a 'curare cleft' (a dip or notch occurring during the latter half of Phase III on a capnogram) indicate?",
        "options": ["Severe bronchospasm and wheezing", "Return of spontaneous diaphragmatic efforts in a patient under neuromuscular blockade, indicating waning muscle relaxation", "A leak in the sampling line adapter", "Incompetence of the expiratory unidirectional valve"],
        "correct_index": 1,
        "explanation": "A curare cleft is a downward notch on the alveolar plateau (Phase III). It occurs when neuromuscular blockade begins to wear off and the patient makes a brief, spontaneous diaphragmatic inspiratory effort that entrains CO2-free fresh gas into the sample line.",
        "key_points": [
            "Indicates returning spontaneous diaphragmatic activity.",
            "Signals the need for additional muscle relaxant or ventilator synchrony adjustment.",
            "Disappears once full neuromuscular blockade is restored."
        ],
        "sample_viva_answer": "A curare cleft is a notch in Phase III of the capnogram produced when the patient makes a spontaneous diaphragmatic inspiratory effort, indicating that neuromuscular blockade is wearing off."
    },
    {
        "id": "AT-MF-05",
        "specialty": "Anaesthesia Technology",
        "topic": "Monitoring fundamentals",
        "difficulty": "Intermediate",
        "question": "A 'shark fin' appearance on the capnography waveform (prolonged expiratory upstroke in Phase II with a steep sloped Phase III) is classic for which clinical condition?",
        "options": ["Hyperventilation", "Expiratory airflow obstruction (e.g., severe bronchospasm, asthma, COPD, or partially kinked ETT)", "Accidental extubation into the pharynx", "Rapid recovery from muscle relaxant"],
        "correct_index": 1,
        "explanation": "Bronchospasm or COPD causes unequal airway emptying throughout the lungs. Well-ventilated units empty first (low CO2), while obstructed units empty slowly (high CO2), causing a delayed expiratory upstroke and prolonged sloped Phase III, giving the waveform a characteristic 'shark fin' appearance.",
        "key_points": [
            "Classic 'shark fin' = bronchospasm, COPD, asthma, obstructed ETT.",
            "Phase II upstroke slope is prolonged; alpha angle is widened.",
            "Normalizes following administration of inhaled bronchodilators."
        ],
        "sample_viva_answer": "The 'shark fin' capnogram waveform is diagnostic of expiratory airflow obstruction, such as acute bronchospasm, asthma exacerbation, or a kinked endotracheal tube, due to asynchronous and delayed alveolar emptying."
    },
    {
        "id": "AT-MF-06",
        "specialty": "Anaesthesia Technology",
        "topic": "Monitoring fundamentals",
        "difficulty": "Advanced",
        "question": "Why does carboxyhemoglobin (CO-Hb) cause dangerously misleading pulse oximeter readings in a smoke inhalation patient?",
        "options": ["The oximeter displays zero immediately", "Carboxyhemoglobin absorbs red light at 660 nm identically to oxyhemoglobin, causing the standard two-wavelength pulse oximeter to read falsely normal (e.g., 99%) despite life-threatening cellular hypoxia", "Carboxyhemoglobin damages the infrared LED sensor diode", "The plethysmograph waveform flattens completely"],
        "correct_index": 1,
        "explanation": "Standard pulse oximeters measure absorbance only at 660 nm and 940 nm. Carboxyhemoglobin has an absorption spectrum at 660 nm virtually identical to oxyhemoglobin. The oximeter interprets CO-Hb as oxy-Hb, displaying a falsely reassuring SpO2 of 98-100%. A co-oximeter is required for true measurement.",
        "key_points": [
            "CO-Hb absorbs 660 nm light like oxy-Hb -> falsely normal SpO2 (~98-100%).",
            "Methemoglobin absorbs 660 nm and 940 nm equally -> locks reading near 85%.",
            "Co-oximeter (multi-wavelength) is mandatory in smoke inhalation and suspected toxicity."
        ],
        "sample_viva_answer": "Carboxyhemoglobin absorbs light at 660 nm almost identically to oxyhemoglobin. Standard two-wavelength pulse oximeters cannot distinguish between the two, resulting in falsely elevated SpO2 readings of 98-100% despite severe tissue hypoxia."
    },
    {
        "id": "AT-MF-07",
        "specialty": "Anaesthesia Technology",
        "topic": "Monitoring fundamentals",
        "difficulty": "Intermediate",
        "question": "Where is the anatomical zero reference point (phlebostatic axis) for leveling an invasive arterial blood pressure transducer in a supine surgical patient?",
        "options": ["External auditory meatus", "Fourth intercostal space at the mid-axillary line (approximating right atrium level)", "Suprasternal notch", "Xiphoid process"],
        "correct_index": 1,
        "explanation": "The phlebostatic axis is located at the intersection of the fourth intercostal space and the mid-axillary line (or mid-anterior-posterior chest diameter). It reflects the level of the right and left atria. For every 10 cm the transducer is placed below the axis, pressure reads falsely high by ~7.5 mmHg (and vice versa).",
        "key_points": [
            "Level: 4th intercostal space, mid-axillary line.",
            "Hydrostatic error: ~0.75 mmHg per cm height difference (or ~7.5 mmHg per 10 cm).",
            "In sitting craniotomy, level transducer to external auditory meatus to reflect circle of Willis perfusion."
        ],
        "sample_viva_answer": "The phlebostatic axis is located at the fourth intercostal space at the mid-axillary line, corresponding to the level of the cardiac atria. Transducers must be zeroed here to eliminate hydrostatic column pressure errors."
    },
    {
        "id": "AT-MF-08",
        "specialty": "Anaesthesia Technology",
        "topic": "Monitoring fundamentals",
        "difficulty": "Advanced",
        "question": "In invasive arterial line monitoring, what does an 'overdamped' waveform indicate on a fast-flush square-wave test?",
        "options": ["A sharp square wave with more than 3 rapid oscillations, overestimating systolic pressure", "A sluggish square wave with zero or less than 1 post-flush oscillation, underestimating true systolic pressure and overestimating diastolic pressure", "A continuous sinusoidal sine wave", "Sudden arterial spasm with absent pulse"],
        "correct_index": 1,
        "explanation": "An overdamped system (caused by air bubbles in tubing, blood clots, kinks, or compliant tubing) absorbs dynamic pressure energy. On a fast-flush test, it shows a blunted square wave with no oscillations, underestimating systolic blood pressure and overestimating diastolic blood pressure (though Mean Arterial Pressure remains accurate).",
        "key_points": [
            "Overdamping causes: air microbubbles, blood clot at catheter tip, compliant tubing.",
            "Overdamped: under-reads systolic, over-reads diastolic; MAP remains reliable.",
            "Underdamping: overshoot with multiple oscillations; over-reads systolic pressure."
        ],
        "sample_viva_answer": "An overdamped arterial line produces a blunted square wave with fewer than one oscillation on fast flush. It under-reads systolic pressure and over-reads diastolic pressure, commonly caused by air bubbles in the transducer tubing or a partial catheter clot."
    },
    {
        "id": "AT-MF-09",
        "specialty": "Anaesthesia Technology",
        "topic": "Monitoring fundamentals",
        "difficulty": "Intermediate",
        "question": "What is the minimum Train-of-Four (TOF) ratio (T4 / T1) required on an adductor pollicis neuromuscular monitor to ensure safe extubation and adequate recovery from non-depolarizing muscle relaxants?",
        "options": ["0.25 (25%)", "0.50 (50%)", "0.70 (70%)", "0.90 (90%)"],
        "correct_index": 3,
        "explanation": "Clinical trials show that a TOF ratio >= 0.90 (90%) measured quantitatively at the adductor pollicis muscle is mandatory to ensure adequate recovery of pharyngeal tone, protective airway reflexes, and prevention of post-operative residual curarization (PORC) and aspiration.",
        "key_points": [
            "TOF ratio >= 0.90 (90%) required for safe extubation.",
            "Subjective manual feeling of 4 twitches can miss TOF ratios between 0.4 and 0.7.",
            "Quantitative acceleromyography or electromyography is strongly recommended."
        ],
        "sample_viva_answer": "A Train-of-Four (TOF) ratio of at least 0.90 (90%) is required before safe extubation to verify adequate recovery of pharyngeal musculature and diaphragmatic strength, preventing post-extubation hypoxemia and aspiration."
    },
    {
        "id": "AT-MF-10",
        "specialty": "Anaesthesia Technology",
        "topic": "Monitoring fundamentals",
        "difficulty": "Beginner",
        "question": "What is the target Bispectral Index (BIS) range indicating adequate depth of general anaesthesia for surgical procedures?",
        "options": ["0 to 20", "40 to 60", "75 to 90", "95 to 100"],
        "correct_index": 1,
        "explanation": "The Bispectral Index (BIS) is a processed EEG monitor scaled from 0 (isoelectric / brain death) to 100 (fully awake). The recommended target range for surgical general anesthesia is 40 to 60, which significantly reduces the risk of intraoperative awareness while avoiding excessively deep anesthesia.",
        "key_points": [
            "100 = Awake; 70-80 = Sedated; 40-60 = Surgical general anesthesia.",
            "< 40 = Deep hypnotic state / burst suppression; 0 = Isoelectric EEG.",
            "Ketamine and nitrous oxide can cause paradoxical BIS elevations."
        ],
        "sample_viva_answer": "The target BIS range during surgical general anaesthesia is 40 to 60. This range ensures adequate hypnosis and amnesia to prevent intraoperative awareness while preventing overly deep anaesthetic depression."
    },
    {
        "id": "AT-MF-11",
        "specialty": "Anaesthesia Technology",
        "topic": "Monitoring fundamentals",
        "difficulty": "Intermediate",
        "question": "In intraoperative 5-lead electrocardiography (ECG), which lead combination provides the highest sensitivity for detecting myocardial ischemia in adult surgical patients?",
        "options": ["Lead I and aVR", "Lead II (arrhythmias and inferior ischemia) and Lead V5 (anterolateral ischemia)", "Lead III and aVL only", "aVR and aVF only"],
        "correct_index": 1,
        "explanation": "Lead II monitors the inferior wall (right coronary artery) and has the largest P wave for arrhythmia analysis. Lead V5 monitors the anterolateral left ventricle (left anterior descending / circumflex coronary arteries). Combining Lead II and Lead V5 detects over 80-90% of intraoperative ischemic episodes.",
        "key_points": [
            "Lead II: inferior ischemia + optimal P-wave view for rhythm analysis.",
            "Lead V5: 5th intercostal space anterior axillary line; detects anterolateral ischemia (~75% sensitive alone).",
            "Combination of II + V5 detects > 80-90% of ischemic events."
        ],
        "sample_viva_answer": "The combination of Lead II and Lead V5 offers the greatest diagnostic sensitivity. Lead II is ideal for rhythm and inferior wall ischemia, while Lead V5 detects anterolateral left ventricular myocardial ischemia."
    },
    {
        "id": "AT-MF-12",
        "specialty": "Anaesthesia Technology",
        "topic": "Monitoring fundamentals",
        "difficulty": "Beginner",
        "question": "What does a significant rise in End-Tidal Carbon Dioxide (PetCO2) during cardiopulmonary resuscitation (CPR) indicate?",
        "options": ["Endotracheal tube has slipped into the bronchus", "Return of Spontaneous Circulation (ROSC)", "Development of tension pneumothorax", "Immediate cessation of brain perfusion"],
        "correct_index": 1,
        "explanation": "During CPR with constant ventilation, PetCO2 reflects cardiac output and pulmonary blood flow. A sudden sustained rise in PetCO2 (often jumping above 35-40 mmHg) is a reliable early physiological indicator of Return of Spontaneous Circulation (ROSC), occurring before a palpable pulse can be felt.",
        "key_points": [
            "PetCO2 < 10 mmHg during CPR indicates inadequate chest compressions.",
            "Sudden spike to 35-40+ mmHg indicates ROSC.",
            "Reflects the immediate restoration of endogenous cardiac output washing CO2 into the lungs."
        ],
        "sample_viva_answer": "An abrupt, sustained increase in PetCO2 during CPR is an established physiological sign of Return of Spontaneous Circulation (ROSC), reflecting the sudden return of systemic cardiac output and pulmonary blood flow."
    }
]

# =========================================================================
# DIALYSIS TECHNOLOGY: Principles & Machine Components (24 questions)
# =========================================================================

DT_PH_QUESTIONS = [
    {
        "id": "DT-PH-01",
        "specialty": "Dialysis Technology",
        "topic": "Principles of hemodialysis",
        "difficulty": "Beginner",
        "question": "What is the primary physical mechanism responsible for the removal of small molecular waste products (such as urea and creatinine) during hemodialysis?",
        "options": ["Electro-osmosis", "Diffusion across a semipermeable membrane driven by a concentration gradient", "Convective thermal filtration", "Active carrier-mediated transport"],
        "correct_index": 1,
        "explanation": "Diffusion is the passive movement of solute molecules down a concentration gradient across a semipermeable membrane. Because dialysate has zero urea and creatinine, these solutes diffuse from blood into the dialysate stream until concentration equilibrium is approached.",
        "key_points": [
            "Diffusion clears small molecules (urea, creatinine, potassium).",
            "Rate of diffusion depends on concentration gradient, membrane surface area, pore size, and temperature.",
            "Counter-current flow maximizes the concentration gradient along the full dialyzer length."
        ],
        "sample_viva_answer": "Diffusion is the main mechanism for clearing small molecular weight toxins like urea. Solutes move passively down their concentration gradient from blood into dialysate across the semipermeable dialyzer membrane."
    },
    {
        "id": "DT-PH-02",
        "specialty": "Dialysis Technology",
        "topic": "Principles of hemodialysis",
        "difficulty": "Intermediate",
        "question": "How does ultrafiltration differ from diffusion in a hemodialyzer circuit?",
        "options": ["Ultrafiltration removes electrolytes only without any water movement", "Ultrafiltration is the bulk movement of water driven by a hydrostatic or osmotic pressure gradient, dragging dissolved solutes by solvent drag", "Ultrafiltration uses active ATP pumps built into the hollow fiber walls", "Ultrafiltration is only used during peritoneal dialysis exchanges"],
        "correct_index": 1,
        "explanation": "Ultrafiltration (UF) is the movement of water across the membrane driven by transmembrane pressure (TMP = hydrostatic pressure difference between blood and dialysate compartments). Solvent drag (convection) accompanies this water movement, clearing middle molecules.",
        "key_points": [
            "Transmembrane Pressure (TMP) drives ultrafiltration.",
            "Water removal rate is set by the machine ultrafiltration controller.",
            "Convection removes middle molecules (e.g., beta-2 microglobulin) alongside bulk fluid movement."
        ],
        "sample_viva_answer": "Ultrafiltration is the removal of fluid (plasma water) driven by transmembrane pressure across the dialyzer membrane, whereas diffusion is the movement of dissolved solutes driven by concentration gradients."
    },
    {
        "id": "DT-PH-03",
        "specialty": "Dialysis Technology",
        "topic": "Principles of hemodialysis",
        "difficulty": "Advanced",
        "question": "What is the physical mechanism of 'convective clearance' (solvent drag) in hemodiafiltration or high-flux hemodialysis?",
        "options": ["Direct electrical attraction of cations to anode plates", "Solutes dissolved in plasma water are carried passively across the membrane alongside bulk fluid movement driven by high ultrafiltration rates", "Active enzymatic breakdown of urea inside hollow fibers", "Microscopic acoustic cavitation in dialysate lines"],
        "correct_index": 1,
        "explanation": "Convection occurs when water moves across a semipermeable membrane under a transmembrane pressure gradient, dragging dissolved solute molecules with it ('solvent drag'). This mechanism is much more effective than diffusion for clearing larger middle molecules like beta-2 microglobulin (11.8 kDa).",
        "key_points": [
            "Convection = bulk fluid flow carrying dissolved solutes (solvent drag).",
            "Independent of concentration gradient; dependent on ultrafiltration rate and sieving coefficient.",
            "Superior for middle molecules (500 to 15,000 Daltons)."
        ],
        "sample_viva_answer": "Convective clearance, or solvent drag, is the process where middle and larger molecular weight toxins are swept across the membrane alongside bulk plasma water driven by high ultrafiltration pressures, rather than relying on slow diffusion gradients."
    },
    {
        "id": "DT-PH-04",
        "specialty": "Dialysis Technology",
        "topic": "Principles of hemodialysis",
        "difficulty": "Intermediate",
        "question": "How is the in vitro solute clearance (K) of a dialyzer mathematically defined during hemodialysis?",
        "options": ["K = Blood Flow Rate * Dialysate Flow Rate", "K = Qb * [(Cbi - Cbo) / Cbi], where Qb is blood flow, Cbi is inlet concentration, and Cbo is outlet concentration", "K = Ultrafiltration Volume / Treatment Time", "K = Transmembrane Pressure / Membrane Thickness"],
        "correct_index": 1,
        "explanation": "Clearance (K) represents the volume of blood completely cleared of a solute per unit of time (mL/min). It is calculated as K = Qb * (Cbi - Cbo) / Cbi, measuring the fraction of solute removed from blood across the dialyzer relative to blood flow rate.",
        "key_points": [
            "Clearance K (mL/min) = Qb * (Cbi - Cbo) / Cbi.",
            "Increases with higher blood flow (Qb) and dialysate flow (Qd).",
            "Plateaus at high flows due to membrane surface area limitations (KoA)."
        ],
        "sample_viva_answer": "Dialyzer clearance is defined as the volume of blood cleared of a given solute per minute, calculated as blood flow rate multiplied by the fractional reduction in solute concentration between the dialyzer inlet and outlet."
    },
    {
        "id": "DT-PH-05",
        "specialty": "Dialysis Technology",
        "topic": "Principles of hemodialysis",
        "difficulty": "Advanced",
        "question": "What is KoA (Mass Transfer Area Coefficient) of a dialyzer and what does it represent?",
        "options": ["The electrical resistance of the casing plastic", "The theoretical maximum clearance (mL/min) of a specific solute at infinite blood and dialysate flow rates, reflecting membrane permeability and surface area", "The rate of dialysate heating", "The pressure drop across the venous bubble trap"],
        "correct_index": 1,
        "explanation": "KoA is an intrinsic property of a dialyzer combining mass transfer coefficient (Ko) and total membrane surface area (A). It represents the maximum achievable clearance of a solute (usually urea) if blood and dialysate flows were infinite, characterizing the dialyzer's diffusive performance.",
        "key_points": [
            "KoA characterizes dialyzer membrane diffusive capacity.",
            "Low-efficiency dialyzer: KoA < 500 mL/min; High-efficiency: KoA > 700-1000 mL/min.",
            "Higher KoA allows high urea clearance even at moderate blood flows."
        ],
        "sample_viva_answer": "KoA, or the mass transfer area coefficient, represents the maximum theoretical clearance of a dialyzer at infinite blood and dialysate flow rates. It reflects both the membrane's surface area and intrinsic permeability to a specific solute."
    },
    {
        "id": "DT-PH-06",
        "specialty": "Dialysis Technology",
        "topic": "Principles of hemodialysis",
        "difficulty": "Beginner",
        "question": "What primary specification classifies a dialyzer as 'high-flux' compared to a 'low-flux' dialyzer?",
        "options": ["High blood pump electrical wattage", "An ultrafiltration coefficient (Kuf) greater than 20 mL/h/mmHg and high clearance of middle molecules (e.g., beta-2 microglobulin)", "Casing made of stainless steel", "Double the length of blood tubing"],
        "correct_index": 1,
        "explanation": "High-flux dialyzers have larger pore sizes, giving them an ultrafiltration coefficient (Kuf) > 20 mL/h/mmHg (compared to < 10 for low-flux) and significant clearance of beta-2 microglobulin. They require precise volumetric ultrafiltration control to avoid excessive fluid loss.",
        "key_points": [
            "High-flux: Kuf > 20 mL/h/mmHg; clears beta-2 microglobulin.",
            "Low-flux: Kuf < 10-15 mL/h/mmHg; limited middle molecule clearance.",
            "High-flux requires volumetric ultrafiltration control and ultra-pure dialysate to prevent backfiltration of endotoxins."
        ],
        "sample_viva_answer": "A high-flux dialyzer has an ultrafiltration coefficient greater than 20 mL/h/mmHg and larger membrane pore sizes that allow significant convective clearance of middle molecules such as beta-2 microglobulin."
    },
    {
        "id": "DT-PH-07",
        "specialty": "Dialysis Technology",
        "topic": "Principles of hemodialysis",
        "difficulty": "Intermediate",
        "question": "Why are synthetic membranes (e.g., polysulfone, polyethersulfone) considered superior in biocompatibility compared to unmodified regenerated cellulose (Cuprophan) membranes?",
        "options": ["Synthetic membranes dissolve into the blood stream safely", "Unmodified cellulose membranes have free hydroxyl groups that activate the alternative complement pathway (C3a, C5a) and induce transient leukopenia and cytokine release", "Synthetic membranes conduct high voltage electric shocks", "Cellulose membranes cannot filter water"],
        "correct_index": 1,
        "explanation": "Unmodified cellulose contains exposed hydroxyl (-OH) groups that vigorously trigger the alternative complement cascade upon contact with blood, producing anaphylatoxins (C3a, C5a) that cause transient pulmonary vascular leukostasis, hypoxemia, and chronic inflammation. Synthetic membranes lack these groups and are highly biocompatible.",
        "key_points": [
            "Cellulose triggers alternative complement pathway (C3a, C5a) -> leukopenia.",
            "Synthetic membranes (polysulfone, PES): minimal complement and neutrophil activation.",
            "Higher biocompatibility reduces chronic inflammation, malnutrition, and cardiovascular morbidity."
        ],
        "sample_viva_answer": "Synthetic membranes like polysulfone have superior biocompatibility because they do not trigger the intense complement activation and acute leukopenia seen with unmodified cellulose membranes containing reactive hydroxyl groups."
    },
    {
        "id": "DT-PH-08",
        "specialty": "Dialysis Technology",
        "topic": "Principles of hemodialysis",
        "difficulty": "Beginner",
        "question": "Why did modern hemodialysis transition universally from acetate-buffered dialysate to bicarbonate-buffered dialysate?",
        "options": ["Acetate caused severe vascular vasodilatation, myocardial depression, nausea, and headache due to slow hepatic conversion to bicarbonate", "Acetate is completely insoluble in water", "Bicarbonate causes blood clotting inside the dialyzer", "Acetate dialysate corrodes PVC tubing"],
        "correct_index": 0,
        "explanation": "Historically, acetate was used because bicarbonate precipitated with calcium and magnesium in single-concentrate jugs. However, acetate caused severe peripheral vasodilation, myocardial suppression, hypoxemia, and symptomatic hypotension. Modern machines use three-stream proportioning to safely mix bicarbonate without precipitation.",
        "key_points": [
            "Acetate causes vasodilation, myocardial depression, and severe intradialytic hypotension.",
            "Bicarbonate is physiological, corrects metabolic acidosis smoothly, and improves hemodynamic stability.",
            "Requires two separate concentrate containers (Acid concentrate with Ca/Mg, and Bicarbonate powder/liquid)."
        ],
        "sample_viva_answer": "Bicarbonate dialysate replaced acetate because acetate caused severe side effects, including peripheral vasodilation, myocardial depression, nausea, and profound hypotension, whereas bicarbonate provides physiological acid-base correction with hemodynamic stability."
    },
    {
        "id": "DT-PH-09",
        "specialty": "Dialysis Technology",
        "topic": "Principles of hemodialysis",
        "difficulty": "Intermediate",
        "question": "What is the clinical rationale for using 'sodium modeling' (sodium profiling) during a hemodialysis treatment?",
        "options": ["To lower patient blood sugar", "To start with higher dialysate sodium (e.g., 145-150 mEq/L) early in the session to support plasma refill rate and blood pressure, then ramp down to lower sodium (136-138 mEq/L) to prevent chronic sodium overload", "To dissolve fibrin clots inside the drip chamber", "To sterilize the effluent dialysate stream"],
        "correct_index": 1,
        "explanation": "Sodium modeling uses high dialysate sodium during early hours when ultrafiltration rates are highest, drawing fluid from the interstitial and intracellular spaces into the vascular bed to maintain blood pressure. It is stepped down later to prevent post-dialysis hypernatremia, thirst, and excessive interdialytic weight gain.",
        "key_points": [
            "Maintains plasma osmolality during rapid initial ultrafiltration.",
            "Reduces intradialytic hypotension, cramping, and disequilibrium symptoms.",
            "Drawback: if end sodium is too high, patient experiences excessive thirst and fluid gain."
        ],
        "sample_viva_answer": "Sodium modeling starts with a higher dialysate sodium concentration early in treatment to maintain vascular volume and prevent hypotension during high fluid removal, tapering down toward normal sodium by the end of dialysis to prevent thirst and fluid overload."
    },
    {
        "id": "DT-PH-10",
        "specialty": "Dialysis Technology",
        "topic": "Principles of hemodialysis",
        "difficulty": "Intermediate",
        "question": "In the standard hemodialysis adequacy formula 'Kt/V', what do K, t, and V represent, and what is the minimum recommended single-pool target per treatment for thrice-weekly dialysis?",
        "options": ["K = Potassium, t = temperature, V = viscosity; target >= 0.5", "K = Dialyzer urea clearance (mL/min), t = treatment time (min), V = patient urea distribution volume (approx. total body water); target spKt/V >= 1.2 (or 1.4 target)", "K = Kinetic energy, t = tension, V = volume; target >= 2.5", "K = Kidney size, t = thrombosis time, V = venous flow; target >= 0.8"],
        "correct_index": 1,
        "explanation": "Kt/V is a dimensionless index of dialysis adequacy. K is dialyzer urea clearance (mL/min), t is treatment duration in minutes, and V is the patient's urea distribution volume (total body water in mL). National KDOQI guidelines recommend a minimum delivered single-pool Kt/V of 1.2 per treatment (target 1.4).",
        "key_points": [
            "Formula: Kt/V (Clearance * Time / Distribution Volume).",
            "Minimum delivered target: spKt/V >= 1.2 per session (target 1.4).",
            "Under-dialysis leads to uremic complications, pericarditis, and increased mortality."
        ],
        "sample_viva_answer": "In Kt/V, K is dialyzer urea clearance, t is treatment time, and V is the patient's urea distribution volume. KDOQI guidelines recommend a minimum delivered single-pool Kt/V of 1.2 per treatment for thrice-weekly hemodialysis."
    },
    {
        "id": "DT-PH-11",
        "specialty": "Dialysis Technology",
        "topic": "Principles of hemodialysis",
        "difficulty": "Beginner",
        "question": "What is the minimum recommended Urea Reduction Ratio (URR) percentage to indicate adequate hemodialysis delivery according to clinical practice guidelines?",
        "options": ["40%", "50%", "65% (target 70%)", "95%"],
        "correct_index": 2,
        "explanation": "URR = [(Pre-BUN - Post-BUN) / Pre-BUN] * 100%. Clinical guidelines mandate a minimum URR of 65% (target 70%), which roughly corresponds to a delivered single-pool Kt/V of 1.2. A post-dialysis blood sample must be drawn using the slow-flow/stop-pump protocol to prevent access recirculation errors.",
        "key_points": [
            "URR = [(Pre - Post) / Pre] * 100%.",
            "Minimum adequate URR is 65%; goal is 70% or higher.",
            "Draw post-BUN using stop-dialysate-flow or slow-blood-pump (100 mL/min) technique."
        ],
        "sample_viva_answer": "The minimum recommended Urea Reduction Ratio is 65%, with a clinical target of 70% or greater, indicating that at least 65% of circulating blood urea nitrogen has been cleared during the session."
    },
    {
        "id": "DT-PH-12",
        "specialty": "Dialysis Technology",
        "topic": "Principles of hemodialysis",
        "difficulty": "Advanced",
        "question": "What is the phenomenon of 'backfiltration' (or backdiffusion) in high-flux hemodialysis?",
        "options": ["Blood flowing backward into the arterial needle", "Movement of dialysate from the dialysate compartment into the blood compartment due to local negative Transmembrane Pressure at the venous end of the dialyzer", "Dialysate escaping through the air bubble trap", "Heparin returning to the syringe pump"],
        "correct_index": 1,
        "explanation": "In high-flux dialyzers with high hydraulic permeability, high ultrafiltration occurs at the blood inlet (positive TMP). Toward the blood outlet, blood pressure drops while dialysate pressure remains higher, creating localized negative TMP that forces non-sterile dialysate backward into the blood compartment (backfiltration). This mandates the use of ultra-pure dialysate (< 0.1 CFU/mL, < 0.03 EU/mL endotoxin).",
        "key_points": [
            "Occurs at distal (venous) end of high-flux dialyzers due to reversed local TMP.",
            "Presents severe risk of endotoxemia and chronic inflammation if dialysate is impure.",
            "Requires pyrogen-retaining ultrafilters and strict water quality standards."
        ],
        "sample_viva_answer": "Backfiltration occurs in high-flux dialyzers when venous blood pressure drops below dialysate pressure, causing dialysate to move backward across the membrane into the bloodstream. It requires ultra-pure dialysate to prevent endotoxin transfer."
    }
]

DT_MC_QUESTIONS = [
    {
        "id": "DT-MC-01",
        "specialty": "Dialysis Technology",
        "topic": "Dialysis machine components",
        "difficulty": "Intermediate",
        "question": "Why is dialysate and blood flow arranged in a 'counter-current' direction inside the hollow-fiber dialyzer?",
        "options": ["To decrease shear stress on red blood cells", "To maintain a continuous concentration gradient for solute diffusion along the entire length of the dialyzer", "To prevent dialysate heater thermostat overheating", "To minimize heparin consumption"],
        "correct_index": 1,
        "explanation": "In counter-current flow, blood flows in the opposite direction of dialysate. This ensures that even as blood loses solute along the fiber, it continuously encounters dialysate with an even lower concentration, maintaining a positive concentration gradient along the entire length and maximizing clearance.",
        "key_points": [
            "Counter-current design maintains concentration gradient end-to-end.",
            "Co-current (parallel) flow would cause diffusion to halt once concentrations equilibrate midway.",
            "Increases dialyzer clearance efficiency by 15-20% compared to concurrent flow."
        ],
        "sample_viva_answer": "Counter-current flow maintains a solute concentration gradient across the entire length of the dialyzer fibers, maximizing diffusion efficiency and clearance compared to co-current flow."
    },
    {
        "id": "DT-MC-02",
        "specialty": "Dialysis Technology",
        "topic": "Dialysis machine components",
        "difficulty": "Beginner",
        "question": "How does the peristaltic roller blood pump deliver blood through the extracorporeal circuit?",
        "options": ["Using centrifugal turbine blades", "By compressing the elastic blood pump segment between two rotating rollers and an outer curved track, propelling a fixed volume forward with each rotation", "Using ultrasonic wave displacement", "Through pressurized pneumatic bladders"],
        "correct_index": 1,
        "explanation": "Peristaltic roller pumps use two opposing rollers that sequentially compress the calibrated blood tubing segment against a semicircular raceway. By continuously occluding the tube and rolling forward, they push forward a predictable volume of blood proportional to pump RPM.",
        "key_points": [
            "Roller occlusion must be calibrated to be barely occlusive (preventing backflow while avoiding hemolysis).",
            "Flow (mL/min) = RPM * stroke volume per revolution.",
            "Excessive roller tightness causes mechanical hemolysis of red blood cells."
        ],
        "sample_viva_answer": "The peristaltic roller pump propels blood by progressively squeezing the flexible tubing against a curved track with rotating rollers, delivering a predictable stroke volume forward with each revolution."
    },
    {
        "id": "DT-MC-03",
        "specialty": "Dialysis Technology",
        "topic": "Dialysis machine components",
        "difficulty": "Intermediate",
        "question": "What is the role of the conductivity cell sensor in the dialysate preparation module of a hemodialysis machine?",
        "options": ["Measures the patient's hematocrit dynamically", "Verifies that acid concentrate, bicarbonate concentrate, and purified water are mixed in the exact proportion to achieve safe ionic concentration", "Monitors the electric grounding of the dialysis reclining chair", "Checks the viscosity of heparin solution"],
        "correct_index": 1,
        "explanation": "The conductivity cell measures the total electrical conductivity of the freshly mixed dialysate (typically 13.5 to 14.5 mS/cm). This verifies that purified water and electrolyte concentrates are proportioned safely, preventing life-threatening hypoosmolar (hemolysis) or hyperosmolar (crenation) complications.",
        "key_points": [
            "Safe dialysate conductivity is typically 13.5 to 14.5 mS/cm (or ~135-145 mmol/L sodium).",
            "Hypoosmolar dialysate causes water entry into RBCs resulting in massive acute hemolysis.",
            "Hyperosmolar dialysate causes severe cellular dehydration and hypernatremia.",
            "If conductivity is outside safe limits, dialysate bypass mode is triggered automatically."
        ],
        "sample_viva_answer": "The conductivity sensor verifies that purified water, acid, and bicarbonate concentrates are blended to the correct electrolyte concentration (13.5-14.5 mS/cm). Incorrect conductivity triggers bypass mode to prevent fatal hemolysis or hyperosmolality."
    },
    {
        "id": "DT-MC-04",
        "specialty": "Dialysis Technology",
        "topic": "Dialysis machine components",
        "difficulty": "Advanced",
        "question": "What is the operating temperature range maintained by the dialysate heater, and what catastrophic event occurs if temperature exceeds 41°C to 42°C?",
        "options": ["20°C to 25°C; causes extreme hyperthermia", "35.5°C to 37.0°C; temperatures > 41°C trigger acute thermal denaturation of red blood cell membrane proteins resulting in massive intravascular hemolysis", "45°C to 50°C; causes dialyzer melting", "30°C to 32°C; causes dialysate freezing"],
        "correct_index": 1,
        "explanation": "Dialysate is kept between 35.5°C and 37°C. If the heater fails and temperature exceeds 41-42°C, thermal denaturation of erythrocyte spectrin and membrane proteins triggers catastrophic acute intravascular hemolysis, hyperkalemia, and cardiovascular collapse.",
        "key_points": [
            "Operating range: 35.5°C to 37.0°C.",
            "> 41°C causes acute thermal hemolysis and fatal hyperkalemia.",
            "Temperatures < 35°C cause patient shivering and vasoconstriction (though mild cool dialysate at 35.5°C improves BP stability)."
        ],
        "sample_viva_answer": "Dialysate is maintained at 35.5°C to 37°C. If temperature exceeds 41°C, thermal hemolysis of red blood cells occurs, releasing massive potassium and free hemoglobin into the circulation, which can be fatal."
    },
    {
        "id": "DT-MC-05",
        "specialty": "Dialysis Technology",
        "topic": "Dialysis machine components",
        "difficulty": "Intermediate",
        "question": "Why is a Deaeration Module (degasser) an essential component in the internal hydraulic circuit of a hemodialysis machine?",
        "options": ["To remove carbon dioxide from patient venous blood directly", "To remove dissolved atmospheric gases that come out of solution when cold incoming water is heated to 37°C, preventing air locks, inaccurate conductivity readings, and microbubbles in dialysate", "To oxygenate the dialysate to 100% saturation", "To inject sterile room air into the drain pipe"],
        "correct_index": 1,
        "explanation": "Cold water holds more dissolved air than warm water. When municipal water is heated to 37°C inside the machine, dissolved air comes out of solution as microscopic bubbles. The deaerator uses negative pressure (vacuum pump) to pull these bubbles out, preventing air locks in flowmeters and erroneous conductivity readings.",
        "key_points": [
            "Heating cold water drives dissolved air out of solution.",
            "Vacuum chamber pulls dissolved microbubbles out before proportioning.",
            "Prevents interference with conductivity cells, flow sensors, and membrane clearance."
        ],
        "sample_viva_answer": "The deaeration module removes dissolved air from water as it is heated to 37°C. Without deaeration, air bubbles would form in the dialysate lines, interfering with conductivity sensors, flowmeters, and dialyzer membrane contact."
    },
    {
        "id": "DT-MC-06",
        "specialty": "Dialysis Technology",
        "topic": "Dialysis machine components",
        "difficulty": "Beginner",
        "question": "What is the function of the automated Dialysate Bypass Valve during an alarm state (e.g., conductivity or temperature error)?",
        "options": ["It increases blood flow rate to 500 mL/min", "It immediately redirects un-safe dialysate away from the dialyzer directly into the drain, protecting the patient's blood from exposure", "It dumps all patient blood into the waste reservoir", "It injects saline into the dialyzer hollow fibers"],
        "correct_index": 1,
        "explanation": "If dialysate conductivity, pH, or temperature violates safe physiological limits, the bypass valve immediately actuates. It diverts the flow of dialysate away from the dialyzer and sends it directly to the drain, isolating the patient's blood until normal parameters are re-established.",
        "key_points": [
            "Isolates dialyzer from unsafe dialysate during alarm states.",
            "Diverts dialysate to drain without interrupting extracorporeal blood flow.",
            "Protects patient from acute hemolysis, crenation, or thermal shock."
        ],
        "sample_viva_answer": "The dialysate bypass valve automatically diverts dialysate away from the dialyzer directly to the drain whenever conductivity or temperature goes out of safe range, protecting the patient from receiving unsafe fluid."
    },
    {
        "id": "DT-MC-07",
        "specialty": "Dialysis Technology",
        "topic": "Dialysis machine components",
        "difficulty": "Intermediate",
        "question": "What does the Transmembrane Pressure (TMP) sensor monitor in a hemodialysis system?",
        "options": ["The rotational speed of the blood pump rollers", "The pressure difference across the dialyzer semipermeable membrane between the blood compartment and the dialysate compartment", "The air pressure inside the venous drip chamber", "The hydraulic pressure in the water treatment sand filter"],
        "correct_index": 1,
        "explanation": "TMP = [(Blood Inlet Pressure + Blood Outlet Pressure) / 2] - [(Dialysate Inlet Pressure + Dialysate Outlet Pressure) / 2]. It measures the hydrostatic gradient driving water across the membrane. A rising TMP indicates dialyzer clotting or high ultrafiltration demand.",
        "key_points": [
            "TMP drives ultrafiltration across the membrane.",
            "Elevated TMP indicates clotting of dialyzer hollow fibers or high fluid removal goals.",
            "Monitored continuously by machine pressure transducers."
        ],
        "sample_viva_answer": "The TMP sensor monitors the hydrostatic pressure gradient between the blood compartment and the dialysate compartment across the dialyzer membrane, which dictates the rate of ultrafiltration."
    },
    {
        "id": "DT-MC-08",
        "specialty": "Dialysis Technology",
        "topic": "Dialysis machine components",
        "difficulty": "Beginner",
        "question": "Where is the automated heparin syringe infusion line typically connected in the extracorporeal blood tubing circuit?",
        "options": ["Downstream of the venous drip chamber directly before blood re-enters the patient", "Upstream of the dialyzer on the arterial blood line (pre-dialyzer) after the blood pump", "Directly into the dialysate supply tubing", "Into the reverse osmosis inlet pipe"],
        "correct_index": 1,
        "explanation": "The heparin infusion line connects to the arterial line downstream of the blood roller pump but upstream of the dialyzer. This ensures that anticoagulant is thoroughly mixed with blood before entering the high-surface-area hollow fibers where clotting risk is greatest.",
        "key_points": [
            "Infused pre-dialyzer to prevent fiber clotting.",
            "Placed post-blood pump so the pump does not compress the heparin infusion line.",
            "Turned off 30 to 60 minutes before the end of treatment to allow hemostasis at needle sites."
        ],
        "sample_viva_answer": "The heparin infusion connects to the arterial blood line after the blood pump and before the dialyzer, ensuring blood is anticoagulated before entering the hollow fibers where clotting is most likely to occur."
    },
    {
        "id": "DT-MC-09",
        "specialty": "Dialysis Technology",
        "topic": "Dialysis machine components",
        "difficulty": "Intermediate",
        "question": "What is the primary function of the mesh filter screen located inside the venous drip chamber?",
        "options": ["To filter out excess sodium ions", "To trap fibrin strands, micro-clots, and debris before blood is returned to the patient, preventing thromboembolism", "To separate red cells from plasma", "To warm the returning blood to 40°C"],
        "correct_index": 1,
        "explanation": "The venous drip chamber includes a fine nylon or polyester mesh filter (typically 100-200 microns). It acts as a safety barrier to trap micro-thrombi, fibrin nets, and particulate matter that may have formed in the dialyzer before blood returns to the patient's venous access.",
        "key_points": [
            "Traps fibrin clots and aggregates before blood re-enters patient.",
            "Fluid level must be kept 2/3 full to prevent air vortexing and microbubble formation.",
            "Clotted filters increase venous pressure alarms and require line change."
        ],
        "sample_viva_answer": "The mesh filter screen inside the venous drip chamber captures fibrin clots and particulate debris generated in the circuit, preventing pulmonary emboli or vascular access thrombosis."
    },
    {
        "id": "DT-MC-10",
        "specialty": "Dialysis Technology",
        "topic": "Dialysis machine components",
        "difficulty": "Advanced",
        "question": "What is the significance of measuring pre-pump arterial pressure in the extracorporeal blood circuit?",
        "options": ["It measures systemic arterial cardiac pressure", "It measures the negative suction pressure generated by the blood pump pulling blood from the vascular access; excessively negative pressure indicates needle collapse or access stenosis", "It detects air bubbles entering the venous chamber", "It calibrates the heparin infusion pump rate"],
        "correct_index": 1,
        "explanation": "The pre-pump arterial pressure transducer is located between the patient's arterial needle and the blood pump. Because the pump draws blood under negative suction, this pressure is negative (normally -50 to -150 mmHg). Pressures more negative than -200 to -250 mmHg cause blood foaming, severe mechanical hemolysis, and fistula collapse.",
        "key_points": [
            "Normally negative (-50 to -150 mmHg).",
            "Excessively negative (< -200 mmHg) causes mechanical hemolysis and indicates access inflow obstruction.",
            "Causes: needle positioned against vessel wall, kinked arterial line, or access stenosis."
        ],
        "sample_viva_answer": "Pre-pump arterial pressure reflects the suction pressure between the access needle and blood pump. If it becomes excessively negative (e.g., beyond -200 mmHg), it indicates inflow obstruction and causes shear stress that can hemolyze red blood cells."
    },
    {
        "id": "DT-MC-11",
        "specialty": "Dialysis Technology",
        "topic": "Dialysis machine components",
        "difficulty": "Beginner",
        "question": "By international convention, what are the standardized colors designating the arterial blood line and venous blood line in hemodialysis tubing sets?",
        "options": ["Arterial is Blue; Venous is Red", "Arterial is Red; Venous is Blue", "Arterial is Green; Venous is Yellow", "Arterial is Black; Venous is White"],
        "correct_index": 1,
        "explanation": "By universal healthcare convention, the Arterial line (taking blood from the patient to the dialyzer) is color-coded RED, and the Venous line (returning cleansed blood from the dialyzer to the patient) is color-coded BLUE.",
        "key_points": [
            "Arterial = RED (blood from patient toward dialyzer).",
            "Venous = BLUE (blood returning to patient).",
            "Standardized on blood lines, needle hubs, and machine transducer ports."
        ],
        "sample_viva_answer": "The arterial blood line is standardized as RED, taking blood from the patient to the dialyzer, while the venous blood line is BLUE, returning cleansed blood back to the patient."
    },
    {
        "id": "DT-MC-12",
        "specialty": "Dialysis Technology",
        "topic": "Dialysis machine components",
        "difficulty": "Advanced",
        "question": "What is the function of the Balancing Chamber (or volumetric UF control system) in modern closed-hydraulic hemodialysis machines?",
        "options": ["To equalize atmospheric pressure on the circuit", "To ensure that the volume of fresh dialysate entering the dialyzer exactly equals the volume of spent dialysate exiting, so that fluid removal is governed strictly by an independent ultrafiltration pump", "To balance the patient's hemoglobin concentration", "To prevent electricity leaks through the drain"],
        "correct_index": 1,
        "explanation": "Modern dialysis machines use volumetric balancing chambers separated by flexible diaphragms. When fresh dialysate enters one chamber, an exact matching volume of spent dialysate leaves the opposite chamber (equal volume in = equal volume out). Fluid removal from the patient is achieved by a separate ultrafiltration removal pump that withdraws a precise volume, ensuring ultrafiltration accuracy within +/- 1%.",
        "key_points": [
            "Ensures volumetric matching of fresh and spent dialysate.",
            "Ultrafiltration is controlled by a dedicated ultrafiltration metering pump.",
            "Prevents uncontrolled fluid gain or loss, protecting against hypovolemic shock."
        ],
        "sample_viva_answer": "The balancing chamber system ensures that fresh dialysate inflow exactly matches spent dialysate outflow. This allows an independent ultrafiltration pump to remove a precise, measured volume of fluid from the patient without fluid error."
    }
]

# =========================================================================
# DIALYSIS TECHNOLOGY: Alarm Recognition & Safety (24 questions)
# =========================================================================

DT_AR_QUESTIONS = [
    {
        "id": "DT-AR-01",
        "specialty": "Dialysis Technology",
        "topic": "Basic alarm recognition",
        "difficulty": "Beginner",
        "question": "What immediate automated actions does a modern hemodialysis machine perform when the Venous Line Air Detector triggers an alarm?",
        "options": ["Increases dialysate flow rate to wash out the bubble", "Clamps the venous line clamp and stops the blood pump to prevent air embolism to the patient", "Diverts dialysate to drain without affecting the blood circuit", "Flushes 500 mL normal saline into the arterial line"],
        "correct_index": 1,
        "explanation": "Air in the venous line presents an immediate risk of fatal air embolism to the patient. The machine's ultrasonic air bubble detector immediately stops the blood pump, clamps the venous blood line clamp, and sounds an audible and visual high-priority alarm.",
        "key_points": [
            "Immediate blood pump stop + venous line clamp closure.",
            "Protects patient against venous air embolism.",
            "Technologist must inspect drip chamber, clear microbubbles, and ensure fluid level is appropriate before resetting."
        ],
        "sample_viva_answer": "When the venous air detector trips, the machine immediately stops the blood pump and closes the venous line clamp to prevent air from entering the patient's bloodstream and causing an air embolism."
    },
    {
        "id": "DT-AR-02",
        "specialty": "Dialysis Technology",
        "topic": "Basic alarm recognition",
        "difficulty": "Advanced",
        "question": "An optical Blood Leak Detector in the effluent dialysate line triggers an alarm. What is the fundamental fault, and what safety response occurs?",
        "options": ["Air is leaking into the bicarbonate proportioning system", "Rupture or breach in the dialyzer semipermeable hollow fibers allowing blood into the dialysate compartment, prompting blood pump shutdown", "Saline infusion bag is depleted", "Water treatment reverse osmosis membrane has failed"],
        "correct_index": 1,
        "explanation": "A blood leak detector uses a photodetector or beam of light across the effluent dialysate line. If dialyzer hollow fibers rupture, red blood cells escape into the dialysate. The optical sensor detects hemoglobin/turbidity, stops the blood pump, and prevents further blood loss and contamination.",
        "key_points": [
            "Detects hollow fiber rupture inside the dialyzer.",
            "Can be confirmed with a chemical blood test strip (hemastix) on the effluent dialysate.",
            "If true leak, treatment must be halted immediately and blood in the circuit must NOT be reinfused to avoid contamination."
        ],
        "sample_viva_answer": "A blood leak alarm indicates a tear or breach in the dialyzer hollow fibers, allowing blood to cross into the effluent dialysate. The machine halts the blood pump, and blood must not be reinfused if a true leak is confirmed."
    },
    {
        "id": "DT-AR-03",
        "specialty": "Dialysis Technology",
        "topic": "Basic alarm recognition",
        "difficulty": "Intermediate",
        "question": "What is the most common cause of a High Venous Pressure alarm during a hemodialysis session?",
        "options": ["Needle dislodged on the bedroom floor", "Kink in the venous return blood tubing, a clot inside the venous drip chamber filter, or venous access stenosis/infiltration", "Low dialysate temperature", "Empty heparin syringe"],
        "correct_index": 1,
        "explanation": "Venous pressure measures resistance to returning blood to the patient. A high venous pressure alarm (> 200-250 mmHg) occurs when return flow is obstructed by a kinked venous line, a clotted drip chamber mesh, a displaced venous needle infiltrating tissue, or venous outflow stenosis in the vascular access.",
        "key_points": [
            "Normal venous pressure: ~100 to 180 mmHg at standard blood flows (300-400 mL/min).",
            "High alarm causes: line kink, infiltration, needle against wall, venous stenosis, clotted filter.",
            "Immediate check: inspect tubing from drip chamber to needle, check needle site for swelling."
        ],
        "sample_viva_answer": "A high venous pressure alarm is commonly caused by an obstruction in the return blood path, such as a kinked venous line, a blood clot in the venous drip chamber filter, needle infiltration into subcutaneous tissue, or stenosis in the patient's venous outflow tract."
    },
    {
        "id": "DT-AR-04",
        "specialty": "Dialysis Technology",
        "topic": "Basic alarm recognition",
        "difficulty": "Intermediate",
        "question": "What does a sudden Low Venous Pressure alarm indicate, and why is it considered a life-threatening emergency?",
        "options": ["Dialysate conductivity is too high", "Venous needle dislodgement or tubing separation, which can result in fatal patient exsanguination within minutes if the blood pump continues running", "Fistula is overly mature", "Saline flush completed"],
        "correct_index": 1,
        "explanation": "A drop in venous pressure below the lower alarm threshold indicates a loss of resistance in the return circuit—most dangerously, venous needle dislodgement from the access or tubing disconnection. At blood flows of 300-450 mL/min, complete exsanguination and fatal hemorrhagic shock can occur in less than 3 to 5 minutes.",
        "key_points": [
            "Life-threatening emergency: venous needle dislodgement or line disconnection.",
            "Can cause fatal blood loss in 3-5 minutes.",
            "Machine halts blood pump immediately upon low venous pressure trigger."
        ],
        "sample_viva_answer": "A sudden low venous pressure alarm indicates a loss of resistance in the return line, most dangerously venous needle dislodgement or circuit separation. Because the blood pump could rapidly exsanguinate the patient, it triggers an immediate pump stop."
    },
    {
        "id": "DT-AR-05",
        "specialty": "Dialysis Technology",
        "topic": "Basic alarm recognition",
        "difficulty": "Intermediate",
        "question": "If the arterial pre-pump pressure alarms at -260 mmHg (excessively negative), what is the appropriate immediate troubleshooting response?",
        "options": ["Increase blood pump speed to 500 mL/min", "Reduce blood pump speed, check the arterial line for kinks, and verify the arterial needle position and patency", "Flush 100 mL of air through the arterial port", "Turn off the water treatment RO system"],
        "correct_index": 1,
        "explanation": "Excessively negative arterial pressure indicates that the blood pump is demanding more blood than the access can supply. Immediate steps: reduce blood pump speed to lower negative suction pressure, inspect the arterial line for kinks, and reposition the arterial needle if it is sucking against the vessel wall.",
        "key_points": [
            "Excessive negative pressure (> -200 to -250 mmHg) causes mechanical hemolysis.",
            "Immediate action: decrease blood pump speed, inspect for kinks, adjust needle position.",
            "Never ignore: prolonged high negative pressure hemolyzes red blood cells."
        ],
        "sample_viva_answer": "When arterial pressure alarms excessively negative, immediately reduce blood pump speed to relieve suction, inspect the line for clamps or kinks, and assess the arterial needle to ensure it is not suctioned against the vessel wall."
    },
    {
        "id": "DT-AR-06",
        "specialty": "Dialysis Technology",
        "topic": "Basic alarm recognition",
        "difficulty": "Advanced",
        "question": "What life-threatening clinical catastrophe occurs if a hemodialysis patient is accidentally exposed to low-conductivity (hypotonic / hypoosmolar) dialysate due to a bypassed or failed conductivity sensor?",
        "options": ["Severe hypernatremic dehydration", "Massive acute intravascular hemolysis and cerebral edema due to water rushing into red blood cells and brain cells down an osmotic gradient", "Immediate metabolic alkalosis with hypokalemia", "Sudden clotting of all extracorporeal tubing"],
        "correct_index": 1,
        "explanation": "Hypoosmolar dialysate has a lower solute concentration than plasma. Water rapidly moves across the dialyzer membrane into blood and red blood cells down the osmotic gradient. RBCs swell and burst (acute intravascular hemolysis), releasing free hemoglobin and potassium (causing fatal cardiac arrhythmias), while water entering brain cells causes cerebral edema and seizures.",
        "key_points": [
            "Hypotonic dialysate causes water entry into RBCs -> massive hemolysis.",
            "Free hemoglobin turns plasma cherry-red/port-wine color; hyperkalemia triggers cardiac arrest.",
            "Safety: conductivity cells trigger automated dialysate bypass to protect patient."
        ],
        "sample_viva_answer": "Exposure to hypotonic dialysate causes massive acute intravascular hemolysis and cerebral edema as water rushes into red blood cells and tissues down the osmotic gradient, leading to life-threatening hyperkalemia and cardiac arrest."
    },
    {
        "id": "DT-AR-07",
        "specialty": "Dialysis Technology",
        "topic": "Basic alarm recognition",
        "difficulty": "Intermediate",
        "question": "What is the danger of high-conductivity (hypertonic) dialysate to the patient if the machine fails to bypass?",
        "options": ["Acute hypothermia", "Hypernatremia, cellular dehydration (crenation of red blood cells), extreme thirst, and intracranial hemorrhage from brain cell shrinkage", "Spontaneous heparin reversal", "Air embolism"],
        "correct_index": 1,
        "explanation": "Hypertonic dialysate draws water out of red blood cells and body tissues by osmosis. Red blood cells shrink and shrivel (crenation), while brain cell shrinkage exerts traction on bridging veins, risking intracranial hemorrhage along with severe hypernatremia and hypertension.",
        "key_points": [
            "Hypertonic dialysate draws water out of cells -> cellular dehydration and crenation.",
            "Severe thirst, headache, hypertension, and hypernatremia.",
            "Machine bypasses dialysate when conductivity exceeds ~14.5-15.0 mS/cm."
        ],
        "sample_viva_answer": "Hypertonic dialysate causes severe cellular dehydration and crenation of red blood cells as water is drawn out into the dialysate, resulting in acute hypernatremia, vascular headache, and brain shrinkage."
    },
    {
        "id": "DT-AR-08",
        "specialty": "Dialysis Technology",
        "topic": "Basic alarm recognition",
        "difficulty": "Beginner",
        "question": "If an optical Blood Leak Alarm trips on the dialysis machine, how does the technologist verify whether it is a 'true leak' versus a 'false alarm' caused by microbubbles or dirty optical lens?",
        "options": ["By drinking a sample of effluent fluid", "By testing a sample of effluent dialysate taken from the dialyzer dialysate outlet port with a chemical blood reagent test strip (e.g., Hemastix)", "By raising blood pump speed to maximum", "By turning off the heparin pump for 30 minutes"],
        "correct_index": 1,
        "explanation": "Optical blood leak detectors can trip falsely due to microbubbles or lens film. The technologist takes a syringe sample of effluent dialysate from the dialyzer outlet port and tests it with a hemastix reagent strip. A positive color change confirms red blood cells / free hemoglobin (true leak).",
        "key_points": [
            "Confirm with chemical reagent strip (Hemastix).",
            "True leak (positive strip): discontinue treatment immediately; do NOT reinfuse blood (risk of contamination).",
            "False alarm (negative strip): clear bubbles, inspect/clean optical detector block."
        ],
        "sample_viva_answer": "The technologist draws a sample of effluent dialysate from the dialyzer outlet and tests it with a chemical blood test strip like Hemastix. A positive test confirms a true hollow-fiber rupture."
    },
    {
        "id": "DT-AR-09",
        "specialty": "Dialysis Technology",
        "topic": "Basic alarm recognition",
        "difficulty": "Advanced",
        "question": "If a true blood leak (positive chemical strip test) is confirmed in the dialyzer, what is the mandatory protocol regarding blood reinfusion?",
        "options": ["Reinfuse all blood rapidly with saline push to save patient hematocrit", "Do NOT return or reinfuse the blood in the extracorporeal circuit; discard the blood lines and dialyzer immediately to prevent introducing non-sterile dialysate into the patient", "Add 5000 units of heparin and continue dialysis", "Recirculate blood through a second dialyzer"],
        "correct_index": 1,
        "explanation": "In a true blood leak, hollow fibers are ruptured, breaching the sterile barrier between blood and non-sterile dialysate. Reinfusing blood from the circuit risks introducing endotoxins, bacteria, and non-sterile dialysate into the patient's bloodstream, causing septicemia and severe pyrogenic reactions.",
        "key_points": [
            "Never return blood from a confirmed true blood leak.",
            "Breach of semipermeable membrane exposes blood to non-sterile dialysate.",
            "Clamp lines, disconnect from access, and discard entire dialyzer and blood lines."
        ],
        "sample_viva_answer": "In a confirmed true blood leak, the blood in the circuit must never be returned to the patient. Because the membrane integrity is broken, the blood is considered contaminated with non-sterile dialysate and must be discarded."
    },
    {
        "id": "DT-AR-10",
        "specialty": "Dialysis Technology",
        "topic": "Basic alarm recognition",
        "difficulty": "Intermediate",
        "question": "What is the primary cause of a Transmembrane Pressure (TMP) high alarm occurring midway through a hemodialysis session?",
        "options": ["The patient fell asleep", "Progressive clotting and deposition of fibrin across the dialyzer hollow fibers, or an excessively high ultrafiltration rate goal", "Low temperature of dialysate", "Air bubble in the arterial needle"],
        "correct_index": 1,
        "explanation": "TMP is the pressure gradient driving fluid across the membrane. When hollow fibers clot with fibrin or protein cakes on the membrane, higher pressure is required to remove fluid, causing TMP to climb. A high ultrafiltration rate goal also drives TMP up.",
        "key_points": [
            "TMP rises as dialyzer fibers clot or fiber bundle volume decreases.",
            "Also caused by high ultrafiltration rates relative to dialyzer Kuf.",
            "Visual check: look for dark streaking or clot formation in dialyzer header."
        ],
        "sample_viva_answer": "A high TMP alarm is primarily caused by clotting and fibrin deposition within the dialyzer hollow fibers, reducing effective surface area, or by attempting an excessively high ultrafiltration rate."
    },
    {
        "id": "DT-AR-11",
        "specialty": "Dialysis Technology",
        "topic": "Basic alarm recognition",
        "difficulty": "Beginner",
        "question": "What does a Water Supply Failure alarm indicate on a hemodialysis machine?",
        "options": ["Patient is dehydrated", "The machine has lost incoming treated purified reverse osmosis (RO) water pressure from the central water treatment plant", "Bicarbonate powder container is empty", "Venous clamp is closed"],
        "correct_index": 1,
        "explanation": "Hemodialysis machines require a continuous supply of treated reverse osmosis water at ~20-30 psi (consuming ~500 mL/min). A water supply alarm indicates loss of water delivery from the central RO loop, triggering machine standby or bypass mode.",
        "key_points": [
            "Indicates loss of inlet water pressure from RO treatment plant.",
            "Machine pauses dialysate production and enters standby mode.",
            "Technologist must verify central RO booster pump and inlet valves."
        ],
        "sample_viva_answer": "A water supply failure alarm indicates that incoming treated water pressure from the central reverse osmosis system has dropped below operational thresholds, pausing dialysate preparation."
    },
    {
        "id": "DT-AR-12",
        "specialty": "Dialysis Technology",
        "topic": "Basic alarm recognition",
        "difficulty": "Advanced",
        "question": "What is the difference between an ultrasonic air sensor detecting 'gross air' versus 'microbubble foam' in the venous blood return line?",
        "options": ["Gross air is silent; microbubbles sound an alarm", "Gross air represents a large continuous air column that triggers immediate clamp closure; microbubble foam represents fine emulsified bubbles that some sensors detect via cumulative sound attenuation, preventing insidious microemboli", "Microbubbles are treated by increasing dialysate flow", "Gross air is normal during hemodialysis"],
        "correct_index": 1,
        "explanation": "Gross air (a bolus of air > 0.1 mL) completely disrupts ultrasonic transmission, triggering instantaneous pump stoppage and venous line clamping. Modern sensors also detect fine microbubble foam by monitoring cumulative acoustic wave attenuation, preventing diffuse pulmonary micro-embolization.",
        "key_points": [
            "Gross air: sudden complete acoustic interruption (> 0.1-0.2 mL bolus).",
            "Microbubble foam: gradual acoustic attenuation from emulsified air/blood foam.",
            "Both trigger venous clamp closure to protect the pulmonary vasculature."
        ],
        "sample_viva_answer": "Gross air is a large discrete air bolus that completely blocks ultrasonic signals, whereas microbubble foam consists of tiny emulsified bubbles that attenuate acoustic signals cumulatively. Both are detected by ultrasonic sensors to prevent air embolism."
    }
]

DT_IP_QUESTIONS = [
    {
        "id": "DT-IP-01",
        "specialty": "Dialysis Technology",
        "topic": "Infection prevention and equipment safety",
        "difficulty": "Beginner",
        "question": "Before cannulation of an arteriovenous (AV) fistula or graft, what is the mandatory physical examination step performed by the dialysis technologist?",
        "options": ["Check for thrill by palpation and bruit by auscultation", "Perform immediate venous pressure calibration with a 10 mL syringe", "Inject 5000 units of heparin directly into the aneurysm", "Apply high-pressure pneumatic tourniquet for 30 minutes"],
        "correct_index": 0,
        "explanation": "Before cannulation, the vascular access must be examined by inspection (signs of infection, aneurysms, skin breakdown), palpation (checking for a continuous soft thrill), and auscultation (listening for a continuous low-pitched whooshing bruit). Absence of thrill or bruit indicates thrombosis.",
        "key_points": [
            "Look (inspection), Feel (palpate thrill), Listen (auscultate bruit).",
            "A high-pitched or discontinuous bruit indicates vascular stenosis.",
            "Never cannulate an infected, thrombosed, or severely stenotic access site."
        ],
        "sample_viva_answer": "The technologist must inspect the access site, palpate for a continuous soft thrill, and auscultate for a continuous low-pitched bruit to confirm vascular patency before cannulating an AV fistula or graft."
    },
    {
        "id": "DT-IP-02",
        "specialty": "Dialysis Technology",
        "topic": "Infection prevention and equipment safety",
        "difficulty": "Advanced",
        "question": "According to AAMI/ISO standards for hemodialysis water quality, why is total chlorine (free chlorine plus chloramines) strictly tested prior to each shift of hemodialysis treatments?",
        "options": ["Chlorine prevents dialyzer fiber clotting", "Chlorine and chloramines cause severe oxidative stress, methemoglobinemia, and acute intravascular hemolysis in dialysis patients", "Chlorine damages the blood tubing plasticizer", "Chlorine impairs conductivity cell calibration"],
        "correct_index": 1,
        "explanation": "Chlorine and chloramines easily cross dialyzer hollow fibers into the bloodstream. Because dialysis patients are exposed to ~360 liters of water per week, residual chloramines cause fatal oxidation of red blood cell membrane lipids and hemoglobin, triggering acute intravascular hemolysis and methemoglobinemia. Maximum allowed level is < 0.1 mg/L.",
        "key_points": [
            "Tested downstream of the primary carbon filter before every patient shift.",
            "Carbon filtration (adsorption) removes chlorine and chloramines.",
            "Maximum permissible total chlorine level is < 0.1 mg/L (ppm).",
            "Breakthrough requires switching to secondary carbon bed and investigating immediately."
        ],
        "sample_viva_answer": "Total chlorine must be below 0.1 mg/L. Residual chlorine and chloramines cross dialyzer membranes and cause severe oxidative hemolysis and methemoglobinemia in patients. It is checked before every treatment shift downstream of the primary carbon filter."
    },
    {
        "id": "DT-IP-03",
        "specialty": "Dialysis Technology",
        "topic": "Infection prevention and equipment safety",
        "difficulty": "Intermediate",
        "question": "How is the 'Percent Rejection' of a Reverse Osmosis (RO) membrane system calculated to assess membrane integrity?",
        "options": ["Percent Rejection = Product TDS / Feed TDS", "Percent Rejection = [1 - (Product TDS / Feed TDS)] * 100%", "Percent Rejection = Feed TDS * Product Flow Rate", "Percent Rejection = Ultrafiltration Rate / Kuf"],
        "correct_index": 1,
        "explanation": "Percent rejection measures the efficiency of the RO membrane in stripping dissolved ionic contaminants from feed water. Calculated as: [1 - (Product Water TDS / Feed Water TDS)] * 100%. A healthy RO membrane should achieve >= 95% to 98% rejection.",
        "key_points": [
            "Formula: [1 - (Product TDS / Feed TDS)] * 100%.",
            "Normal rejection: 95% to 99%.",
            "A drop below 90-95% indicates membrane fouling, chemical degradation, or physical rupture."
        ],
        "sample_viva_answer": "RO percent rejection is calculated as one minus the ratio of product TDS to feed TDS, multiplied by 100%. It measures the percentage of dissolved solids rejected by the membrane and should typically exceed 95%."
    },
    {
        "id": "DT-IP-04",
        "specialty": "Dialysis Technology",
        "topic": "Infection prevention and equipment safety",
        "difficulty": "Intermediate",
        "question": "According to AAMI / ISO 23500 standards, what are the maximum allowable limits for bacteria (CFU/mL) and endotoxin (EU/mL) in standard hemodialysis water?",
        "options": ["Bacteria < 1000 CFU/mL; Endotoxin < 5.0 EU/mL", "Bacteria < 100 CFU/mL; Endotoxin < 0.25 EU/mL", "Bacteria = 0 CFU/mL; Endotoxin = 0 EU/mL (must be completely sterile)", "Bacteria < 500 CFU/mL; Endotoxin < 2.0 EU/mL"],
        "correct_index": 1,
        "explanation": "Under AAMI / ISO 23500 standards, maximum allowable levels for standard dialysis water are < 100 CFU/mL for viable microbial count and < 0.25 EU/mL for bacterial endotoxins (with action levels at 50 CFU/mL and 0.125 EU/mL). For ultra-pure dialysate, limits are < 0.1 CFU/mL and < 0.03 EU/mL.",
        "key_points": [
            "Standard water: Bacteria < 100 CFU/mL; Endotoxin < 0.25 EU/mL.",
            "Action levels: 50 CFU/mL and 0.125 EU/mL.",
            "Ultrapure dialysate: < 0.1 CFU/mL and < 0.03 EU/mL."
        ],
        "sample_viva_answer": "Under AAMI and ISO standards, standard hemodialysis water must contain fewer than 100 CFU/mL of bacteria and an endotoxin concentration under 0.25 EU/mL."
    },
    {
        "id": "DT-IP-05",
        "specialty": "Dialysis Technology",
        "topic": "Infection prevention and equipment safety",
        "difficulty": "Advanced",
        "question": "In centers that practice dialyzer reprocessing (reuse), which chemical agent is commonly used as a germicide for high-level disinfection of hollow-fiber dialyzers?",
        "options": ["Absolute ethanol", "Peracetic acid mixture (Renalin - peracetic acid, hydrogen peroxide, and acetic acid)", "Potassium permanganate", "Dilute hydrochloric acid"],
        "correct_index": 1,
        "explanation": "Peracetic acid-based cold sterilants (e.g., Renalin) are widely used for dialyzer reprocessing. They degrade safely into oxygen, water, and acetic acid without leaving toxic residues, providing high-level sporicidal disinfection with an exposure time of >= 11 hours at 20°C.",
        "key_points": [
            "Peracetic acid (Renalin) degrades to water, oxygen, and acetic acid.",
            "Replaced toxic formaldehyde and glutaraldehyde in modern reuse programs.",
            "Must verify total cell bundle volume (TCBV >= 80% of original) and membrane integrity before reuse."
        ],
        "sample_viva_answer": "Peracetic acid mixtures (such as Renalin, containing peracetic acid, hydrogen peroxide, and acetic acid) are standard for dialyzer reprocessing, providing high-level disinfection that breaks down into harmless water and acetic acid."
    },
    {
        "id": "DT-IP-06",
        "specialty": "Dialysis Technology",
        "topic": "Infection prevention and equipment safety",
        "difficulty": "Intermediate",
        "question": "Prior to connecting a reprocessed (reused) dialyzer to a patient, what mandatory test must be performed by two independent healthcare workers?",
        "options": ["A taste test of the rinse saline", "Testing for complete absence of residual chemical germicide/disinfectant (e.g., peracetic acid or formaldehyde) using sensitive chemical test strips", "Measuring dialyzer weight on a postal scale", "Heating the dialyzer in a microwave oven"],
        "correct_index": 1,
        "explanation": "Before patient connection, the reprocessed dialyzer must be primed and thoroughly rinsed with normal saline. Two qualified clinicians must independently test the rinse saline from both the blood and dialysate ports with sensitive chemical reagent test strips to verify that residual disinfectant is below toxic detection limits.",
        "key_points": [
            "Two-person independent verification required.",
            "Chemical test strips confirm complete washout of germicide.",
            "Failure to rinse germicide causes chemical hemolysis, acute toxic reactions, and tissue necrosis."
        ],
        "sample_viva_answer": "Two independent clinicians must test the saline rinse from the dialyzer with a chemical test strip to verify that residual disinfectant has been completely flushed out before connecting the patient."
    },
    {
        "id": "DT-IP-07",
        "specialty": "Dialysis Technology",
        "topic": "Infection prevention and equipment safety",
        "difficulty": "Beginner",
        "question": "What is the recommended cannulation practice for preserving the long-term integrity of an arteriovenous fistula and preventing pseudoaneurysm formation?",
        "options": ["Cannulate the exact same skin hole repeatedly without blunt needles", "Rope-ladder technique (rotating cannulation sites along the length of the vein with each session) or established Buttonhole technique with blunt needles", "Cannulate only into large dilated aneurysmal sacs", "Always place needles within 1 cm of the surgical anastomosis"],
        "correct_index": 1,
        "explanation": "The rope-ladder technique rotates needle insertion sites across the entire length of the fistula vein, allowing prior puncture sites to heal and preventing vessel wall weakening and pseudoaneurysms. The buttonhole technique uses the exact same track with blunt needles once the tract is mature.",
        "key_points": [
            "Rope-ladder: rotate needle sites along the vessel; allows tissue healing.",
            "Buttonhole: uses constant tract with blunt needles; requires dedicated cannulator.",
            "Cannulating the same area repeatedly (area cannulation) causes aneurysmal dilation and rupture risk."
        ],
        "sample_viva_answer": "The rope-ladder technique, which rotates needle insertion sites along the length of the fistula, prevents vessel wall weakening, stenosis, and pseudoaneurysm formation. Alternatively, the buttonhole technique uses established tracts with blunt needles."
    },
    {
        "id": "DT-IP-08",
        "specialty": "Dialysis Technology",
        "topic": "Infection prevention and equipment safety",
        "difficulty": "Intermediate",
        "question": "According to CDC guidelines, what is the preferred antiseptic solution for cleaning the exit site and hub of a hemodialysis Central Venous Catheter (CVC)?",
        "options": ["Plain sterile water", "Alcoholic chlorhexidine gluconate solution (> 0.5% chlorhexidine in 70% alcohol)", "Normal saline with soap", "Povidone iodine without drying"],
        "correct_index": 1,
        "explanation": "CDC guidelines recommend alcoholic chlorhexidine (> 0.5% chlorhexidine with 70% isopropyl alcohol) for CVC exit site disinfection and catheter hub scrubbing. It provides superior residual bactericidal action compared to aqueous povidone-iodine and must be allowed to air dry completely.",
        "key_points": [
            "Chlorhexidine 2% in 70% isopropyl alcohol is the gold standard.",
            "Must allow full air drying (at least 30-60 seconds) to achieve antimicrobial kill.",
            "Significant reduction in Catheter-Related Bloodstream Infections (CRBSI)."
        ],
        "sample_viva_answer": "CDC guidelines recommend an alcoholic chlorhexidine gluconate solution (> 0.5% chlorhexidine in 70% alcohol) for CVC exit site and hub prep due to its proven efficacy in preventing catheter-related bloodstream infections."
    },
    {
        "id": "DT-IP-09",
        "specialty": "Dialysis Technology",
        "topic": "Infection prevention and equipment safety",
        "difficulty": "Advanced",
        "question": "What is an important safety step performed prior to using an indwelling hemodialysis catheter locked with concentrated heparin (e.g., 5,000 U/mL) or 4% sodium citrate?",
        "options": ["Flush the entire lock volume forcefully into the patient's bloodstream", "Aspirate and discard the exact catheter lumen priming volume along with any small clots prior to flushing with saline", "Infuse 100 mL of normal saline through the lock", "Inject protamine into the catheter hub"],
        "correct_index": 1,
        "explanation": "Catheter lumens contain concentrated anticoagulant (heparin or citrate) matching the lumen priming volume. Flushing this directly into the patient causes systemic anticoagulation or hypocalcemia. The technologist must aspirate and discard the exact lumen volume plus 0.5 mL before flushing.",
        "key_points": [
            "Aspirate and discard catheter lock volume before treatment.",
            "Flushing heparin lock into patient risks systemic bleeding.",
            "Flushing concentrated citrate lock risks acute hypocalcemic cardiac arrest."
        ],
        "sample_viva_answer": "Before initiating treatment, the exact catheter lumen priming volume containing the concentrated heparin or citrate lock must be aspirated and discarded to prevent systemic anticoagulation or citrate-induced hypocalcemia."
    },
    {
        "id": "DT-IP-10",
        "specialty": "Dialysis Technology",
        "topic": "Infection prevention and equipment safety",
        "difficulty": "Beginner",
        "question": "What infection control requirement is mandatory for hemodialysis patients who are Hepatitis B Surface Antigen (HBsAg) positive?",
        "options": ["They cannot undergo hemodialysis under any circumstances", "They must be dialyzed in a separate dedicated isolation room on a dedicated machine with dedicated staff and equipment", "They only require a double dose of heparin", "They must use acetate dialysate"],
        "correct_index": 1,
        "explanation": "Because Hepatitis B virus is transmitted through microscopic blood contamination and survives on environmental surfaces for days, CDC guidelines mandate that HBsAg-positive patients be treated in a separate isolation room on a dedicated machine, with designated supplies and staff.",
        "key_points": [
            "HBsAg positive: dedicated isolation room, dedicated machine, dedicated staff.",
            "HCV and HIV: treated in the general area using standard precautions (isolation not required by CDC).",
            "Routine monthly screening of susceptible patients for HBsAg and anti-HBs titers."
        ],
        "sample_viva_answer": "Hepatitis B surface antigen positive patients must be treated in a separate isolation room using a dedicated hemodialysis machine and dedicated supplies to prevent viral transmission through environmental contamination."
    },
    {
        "id": "DT-IP-11",
        "specialty": "Dialysis Technology",
        "topic": "Infection prevention and equipment safety",
        "difficulty": "Advanced",
        "question": "What is the physiological cause and management of Dialysis Disequilibrium Syndrome (DDS) occurring during a patient's first hemodialysis session?",
        "options": ["Excessive heparin causing subdural hematoma", "Rapid removal of urea from the blood while urea clears slowly from brain tissue, creating a reverse osmotic gradient that draws water into the brain, causing acute cerebral edema", "Hypercalcemia from calcium carbonate", "Air embolism through the dialyzer header"],
        "correct_index": 1,
        "explanation": "Urea passes slowly across the blood-brain barrier. When aggressive dialysis rapidly clears urea from plasma in severely uremic patients, plasma osmolality falls faster than brain osmolality. Water shifts into brain cells down the osmotic gradient, producing cerebral edema, headache, nausea, seizures, and coma. Prevented by short, gentle initial sessions (2 hours, low blood flow ~150-200 mL/min).",
        "key_points": [
            "Cause: rapid plasma urea reduction creates reverse osmotic gradient into brain cells -> cerebral edema.",
            "Symptoms: headache, nausea, restlessness, seizures, obtundation.",
            "Prevention on first dialysis: short duration (2 hrs), low blood flow (150-200 mL/min), low urea clearance."
        ],
        "sample_viva_answer": "Dialysis Disequilibrium Syndrome is caused by rapid clearance of urea from the blood compared to slow clearance from the brain, establishing a reverse osmotic gradient that draws water into cerebral tissue and causes cerebral edema. It is prevented by initiating dialysis with short, low-clearance sessions."
    },
    {
        "id": "DT-IP-12",
        "specialty": "Dialysis Technology",
        "topic": "Infection prevention and equipment safety",
        "difficulty": "Intermediate",
        "question": "What is the difference between Chemical Disinfection and Heat (Thermal) Disinfection cycles on a modern hemodialysis machine?",
        "options": ["Chemical uses liquid sterilants (e.g., sodium hypochlorite, citric acid, or peracetic acid) at ambient temperature; Thermal disinfection circulates water heated to 85°C to 90°C through the internal hydraulic fluid paths", "Thermal disinfection uses open flame burners inside the casing", "Chemical disinfection is only used on the outside plastic cover", "Thermal disinfection cannot destroy bacteria"],
        "correct_index": 0,
        "explanation": "Chemical disinfection introduces chemical agents (citric acid for descaling/disinfection, sodium hypochlorite for bleach cleaning) through the fluid pathways and requires a subsequent rinse to remove all residues. Thermal disinfection circulates heated water (85-90°C) through the hydraulics, effectively destroying bacteria and biofilms without leaving chemical residues.",
        "key_points": [
            "Chemical disinfection: uses citric acid, bleach, or peracetic acid; requires rinse verification.",
            "Thermal disinfection: uses hot water (85-90°C); eliminates chemical exposure risk.",
            "Performed between patient shifts and at the end of each treatment day."
        ],
        "sample_viva_answer": "Chemical disinfection circulates disinfectants like citric acid or bleach through the internal hydraulics to eliminate biofilm and requires a full rinse, whereas thermal disinfection circulates water heated to 85°C to 90°C to achieve sanitization without chemicals."
    }
]

# Compile all questions into a single master list
ALL_QUESTIONS = (
    RT_AP_QUESTIONS + RT_OT_QUESTIONS + RT_VF_QUESTIONS + RT_RE_QUESTIONS +
    AT_EI_QUESTIONS + AT_MC_QUESTIONS + AT_SC_QUESTIONS + AT_MF_QUESTIONS +
    DT_PH_QUESTIONS + DT_MC_QUESTIONS + DT_AR_QUESTIONS + DT_IP_QUESTIONS
)

print(f"Total compiled questions: {len(ALL_QUESTIONS)}")

# Write to questions.py
header = '''"""
MedSkill AI - Reviewed Question Bank (Expanded Curriculum Edition)
Curated educational questions for practical viva preparation in:
1. Respiratory Therapy (4 topics x 12 = 48 questions)
2. Anaesthesia Technology (4 topics x 12 = 48 questions)
3. Dialysis Technology (4 topics x 12 = 48 questions)
Total: 144 verified practical viva questions.

Disclaimer: Educational prototype for healthcare technology students.
Not for clinical decision support or direct patient care.
"""

QUESTIONS_DATA = '''

footer = '''

# Utility lookups and helpers
SPECIALTIES = [
    "Respiratory Therapy",
    "Anaesthesia Technology",
    "Dialysis Technology"
]

TOPICS_BY_SPECIALTY = {
    "Respiratory Therapy": [
        "All Topics",
        "Respiratory anatomy and physiology",
        "Oxygen therapy",
        "Ventilator fundamentals",
        "Respiratory equipment"
    ],
    "Anaesthesia Technology": [
        "All Topics",
        "Anaesthesia equipment identification",
        "Basic machine components",
        "Equipment safety checks",
        "Monitoring fundamentals"
    ],
    "Dialysis Technology": [
        "All Topics",
        "Principles of hemodialysis",
        "Dialysis machine components",
        "Basic alarm recognition",
        "Infection prevention and equipment safety"
    ]
}

SPECIALTY_METADATA = {
    "Respiratory Therapy": {
        "tagline": "Airway, mechanical ventilation, gas therapy & diagnostic monitoring",
        "color": "#0E7490",
        "icon": "lungs",
        "overview": "Master high-flow oxygen devices, ventilator waveforms, pulmonary mechanics, and artificial airway management for practical vivas."
    },
    "Anaesthesia Technology": {
        "tagline": "Workstations, safety systems, scavenging & clinical monitoring",
        "color": "#1D4ED8",
        "icon": "activity",
        "overview": "Revise workstation safety interlocks, vaporizer physics, circle breathing circuits, capnography, and machine pre-use checks."
    },
    "Dialysis Technology": {
        "tagline": "Extracorporeal circuits, dialyzers, alarms & water safety",
        "color": "#047857",
        "icon": "droplet",
        "overview": "Consolidate principles of diffusion, ultrafiltration, alarm handling (air, blood leak, conductivity), and AAMI water treatment protocols."
    }
}


def get_questions_for_specialty(specialty: str, topic: str = "All Topics", difficulty: str = "All Difficulties"):
    """Filter questions based on specialty, topic, and difficulty."""
    filtered = [q for q in QUESTIONS_DATA if q["specialty"] == specialty]
    if topic and topic != "All Topics":
        filtered = [q for q in filtered if q["topic"] == topic]
    if difficulty and difficulty != "All Difficulties":
        filtered = [q for q in filtered if q["difficulty"] == difficulty]
    return filtered


def get_question_by_id(question_id: str):
    """Retrieve question dictionary by its ID."""
    for q in QUESTIONS_DATA:
        if q["id"] == question_id:
            return q
    return None


def get_all_revision_notes_for_topic(specialty: str, topic: str):
    """Return compiled revision key points for a specific specialty and topic."""
    matching = [q for q in QUESTIONS_DATA if q["specialty"] == specialty and q["topic"] == topic]
    notes = []
    for q in matching:
        notes.extend(q.get("key_points", []))
    return list(dict.fromkeys(notes))  # preserve order & remove duplicates
'''

with open("questions.py", "w", encoding="utf-8") as f:
    f.write(header)
    f.write(json.dumps(ALL_QUESTIONS, indent=4))
    f.write(footer)

print("Successfully written questions.py with all 144 questions!")
