import json
from ai_coscientist import AIScientistFramework

ai_coscientist = AIScientistFramework(
    model_name="gemini/gemini-2.0-flash",  # Or "gemini/gemini-2.0-flash" if you have access
    max_iterations=2,  # Reduced iterations for example run
    verbose=False,  # Set to True for detailed logs
    hypotheses_per_generation=10,
    tournament_size=8,
    evolution_top_k=3,
)

# Define a research goal
research_goal = "Develop novel hypotheses for Incentivizing Reasoning Capability in LLMs via Reinforcement Learning"

# Run the research workflow
results = ai_coscientist.run_research_workflow(research_goal)

# Output the results
print("\n--- Research Workflow Results ---")
if "error" in results:
    print(f"Error during workflow: {results['error']}")
else:
    print("\n--- Top Ranked Hypotheses ---")
    for hy in results["top_ranked_hypotheses"]:
        print(f"- Hypothesis: {hy['text']}")
        print(f"  Elo Rating: {hy['elo_rating']}")
        print(f"  Score: {hy['score']:.2f}")
        print(
            f"  Reviews: {hy['reviews'][-1].get('review_summary') if hy['reviews'] else 'No reviews'}"
        )  # Print review summary
        print(
            f"  Similarity Cluster ID: {hy['similarity_cluster_id']}"
        )
        print(
            f"  Win Rate: {hy['win_rate']}% (Matches: {hy['total_matches']})"
        )
        print("-" * 30)

    print("\n--- Meta-Review Insights Summary ---")
    meta_review_summary = results["meta_review_insights"].get(
        "meta_review_summary", "No meta-review summary available."
    )
    print(
        meta_review_summary[:500] + "..."
        if len(meta_review_summary) > 500
        else meta_review_summary
    )  # Print truncated or full summary

    print("\n--- Execution Metrics ---")
    print(json.dumps(results["execution_metrics"], indent=2))
    print(
        f"\nTotal Workflow Time: {results['total_workflow_time']:.2f} seconds"
    )

    if (
        ai_coscientist.verbose
    ):  # Only print full history if verbose is on, can be very long
        print("\n--- Conversation History (Verbose Mode) ---")
        print(
            results["conversation_history"][:1000] + "..."
        )  # Print first 1000 chars of history

# Save agent states (optional)
try:
    ai_coscientist.save_state()
except Exception as e:
    print(f"Error saving state: {e}")
