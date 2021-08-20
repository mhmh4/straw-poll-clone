from .models import Poll


def get_poll_percentages(p: Poll) -> list[str]:
        results = (p.option1_results,
                   p.option2_results,
                   p.option3_results,
                   p.option4_results,
                   p.option5_results)
        total_votes = sum(results)
        if total_votes == 0:
            return [f"{0.0}%"] * 5 
        percentages = []
        for r in results:
            pe = f"{100 * r / total_votes:0.2f}%"
            percentages.append(pe)
        return percentages
