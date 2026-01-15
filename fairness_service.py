def calculate_fairness(sla_data: dict):
    score = 100
    red_flags = []

    # ---- Penalty / Late fee ----
    penalty = sla_data.get("penalty_charges", "").lower()
    if penalty:
        score -= 15
        red_flags.append("Penalty or default charges present")

    # ---- Foreclosure charges ----
    foreclosure = sla_data.get("foreclosure_charges", "").lower()
    if "5%" in foreclosure or "five" in foreclosure:
        score -= 15
        red_flags.append("High foreclosure charges (5%)")

    # ---- Prepayment charges ----
    prepayment = sla_data.get("prepayment_charges", "").lower()
    if prepayment:
        score -= 10
        red_flags.append("Prepayment charges applied")

    # ---- Grace period ----
    grace = sla_data.get("grace_period", "")
    if not grace:
        score -= 15
        red_flags.append("No grace period mentioned")

    # ---- Interest rate ambiguity ----
    interest = sla_data.get("interest_rate", "").lower()
    if "mclr" in interest or "floating" in interest:
        score -= 10
        red_flags.append("Interest rate linked to external benchmark (variable)")

    # ---- Clamp score ----
    score = max(score, 0)

    # ---- Fairness level ----
    if score >= 80:
        level = "Fair"
    elif score >= 60:
        level = "Moderate Risk"
    elif score >= 40:
        level = "High Risk"
    else:
        level = "Unfair"

    return {
        "fairness_score": score,
        "fairness_level": level,
        "red_flags": red_flags
    }
