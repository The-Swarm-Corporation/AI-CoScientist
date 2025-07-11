![AI-CoScientist](https://storage.googleapis.com/gweb-research2023-media/images/AICoScientist-1-Components.width-1250.png)

# AI-CoScientist

[![Join our Discord](https://img.shields.io/badge/Discord-Join%20our%20server-5865F2?style=for-the-badge&logo=discord&logoColor=white)](https://discord.gg/swarms-999382051935506503) [![Subscribe on YouTube](https://img.shields.io/badge/YouTube-Subscribe-red?style=for-the-badge&logo=youtube&logoColor=white)](https://www.youtube.com/@kyegomez3242) [![Connect on LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/kye-g-38759a207/) [![Follow on X.com](https://img.shields.io/badge/X.com-Follow-1DA1F2?style=for-the-badge&logo=x&logoColor=white)](https://x.com/kyegomezb)

A multi-agent AI framework for collaborative scientific research, implementing the "Towards an AI Co-Scientist" methodology with tournament-based hypothesis evolution, peer review systems, and intelligent agent orchestration.

## Features

🧠 **Multi-Agent Architecture**: Specialized agents for hypothesis generation, peer review, ranking, evolution, and meta-analysis  
🏆 **Tournament-Based Selection**: Elo rating system for hypothesis ranking through pairwise comparisons  
📊 **Comprehensive Review System**: Scientific soundness, novelty, testability, and impact assessment  
🔄 **Iterative Refinement**: Meta-review guided evolution with strategic hypothesis improvement  
🎯 **Diversity Control**: Proximity analysis to maintain hypothesis diversity and reduce redundancy  
📈 **Execution Metrics**: Detailed performance tracking and agent timing analytics  
💾 **State Persistence**: Save and resume research workflows with agent state management  
🛡️ **Robust Error Handling**: Graceful fallbacks and recovery mechanisms for production reliability

## Architecture

The AI-CoScientist framework consists of the following components:

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│ Generation      │    │ Reflection      │    │ Ranking         │
│ Agent           │───▶│ Agent           │───▶│ Agent           │
└─────────────────┘    └─────────────────┘    └─────────────────┘
         │                       │                       │
         ▼                       ▼                       ▼
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│ Evolution       │    │ Meta-Review     │    │ Tournament      │
│ Agent           │◀───│ Agent           │    │ Agent           │
└─────────────────┘    └─────────────────┘    └─────────────────┘
         │                       │                       │
         ▼                       ▼                       ▼
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│ Proximity       │    │ Supervisor      │    │ Conversation    │
│ Agent           │    │ Agent           │    │ Manager         │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

### Workflow Process

1. **Generation Phase**: Create initial hypotheses based on research goal
2. **Reflection Phase**: Peer review each hypothesis for scientific merit
3. **Ranking Phase**: Order hypotheses by review scores
4. **Tournament Phase**: Pairwise comparisons with Elo rating updates
5. **Meta-Review Phase**: Synthesize insights across all reviews
6. **Evolution Phase**: Refine top hypotheses based on feedback
7. **Proximity Analysis**: Cluster similar hypotheses for diversity control
8. **Iteration**: Repeat refinement cycles for continuous improvement

## Installation

### Prerequisites

- Python 3.10 or higher
- API access to LLM providers (OpenAI, Anthropic, Google, etc.)

### Install from PyPI

```bash
pip3 install -U ai-coscientist
```

### Install from Source


```bash

git clone https://github.com/The-Swarm-Corporation/AI-CoScientist.git
cd AI-CoScientist
pip install -e .
```

### Environment Setup

Create a `.env` file with your API keys:

```bash
OPENAI_API_KEY=your_openai_key_here
ANTHROPIC_API_KEY=your_anthropic_key_here
GOOGLE_API_KEY=your_google_key_here
```


## Quick Start

```python
from ai_coscientist import AIScientistFramework

# Initialize the AI Co-scientist Framework
ai_coscientist = AIScientistFramework(
    model_name="gpt-4o-mini",
    max_iterations=3,
    hypotheses_per_generation=10,
    tournament_size=8,
    evolution_top_k=3,
    verbose=True
)

# Define your research goal
research_goal = "Develop novel approaches for improving reasoning capabilities in large language models"

# Run the research workflow
results = ai_coscientist.run_research_workflow(research_goal)

# Access the results
print(f"Generated {len(results['top_ranked_hypotheses'])} top hypotheses")
for i, hypothesis in enumerate(results['top_ranked_hypotheses'], 1):
    print(f"{i}. {hypothesis['text']}")
    print(f"   Elo Rating: {hypothesis['elo_rating']}")
    print(f"   Win Rate: {hypothesis['win_rate']}%")
```

---

## Architecture

The AI-CoScientist framework consists of 8 specialized agents:

- **Generation Agent**: Creates novel research hypotheses
- **Reflection Agent**: Peer review and scientific critique
- **Ranking Agent**: Hypothesis ranking and selection
- **Evolution Agent**: Hypothesis refinement and improvement
- **Meta-Review Agent**: Cross-hypothesis insight synthesis
- **Proximity Agent**: Similarity analysis and diversity control
- **Tournament Agent**: Pairwise hypothesis comparison
- **Supervisor Agent**: Workflow orchestration and planning

## Advanced Usage

### Custom Configuration

```python
ai_coscientist = AIScientistFramework(
    model_name="claude-3-sonnet",
    max_iterations=5,
    base_path="./custom_states",
    verbose=True,
    tournament_size=12,
    hypotheses_per_generation=15,
    evolution_top_k=5,
)
```

### State Management

```python
# Save agent states
ai_coscientist.save_state()

# Load previous states
ai_coscientist.load_state()
```

### Results Analysis

```python
results = ai_coscientist.run_research_workflow(research_goal)

# Execution metrics
metrics = results['execution_metrics']
print(f"Total time: {results['total_workflow_time']:.2f}s")
print(f"Hypotheses generated: {metrics['hypothesis_count']}")
print(f"Reviews completed: {metrics['reviews_count']}")
print(f"Tournament rounds: {metrics['tournaments_count']}")

# Meta-review insights
insights = results['meta_review_insights']
print("Strategic recommendations:", insights.get('strategic_recommendations'))
```

## Documentation

For detailed documentation, see [DOCS.md](DOCS.md).


## 🤝 Contributing

We welcome contributions! Please feel free to open an issue or submit a pull request.
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## 📚 Citation

If you use this work in your research, please cite both the original paper and this software implementation.

```bibtex
@article{gottweis2024towards,
    title={Towards an AI co-scientist},
    author={Juraj Gottweis and Wei-Hung Weng and Alexander Daryin and Tao Tu and Anil Palepu and Petar Sirkovic and Artiom Myaskovsky and Felix Weissenberger and Keran Rong and Ryutaro Tanno and Khaled Saab and Dan Popovici and Jacob Blum and Fan Zhang and Katherine Chou and Avinatan Hassidim and Burak Gokturk and Amin Vahdat and Pushmeet Kohli and Yossi Matias and Andrew Carroll and Kavita Kulkarni and Nenad Tomasev and Vikram Dhillon and Eeshit Dhaval Vaishnav and Byron Lee and Tiago R D Costa and José R Penadés and Gary Peltz and Yunhan Xu and Annalisa Pawlosky and Alan Karthikesalingam and Vivek Natarajan},
    year={2024},
    institution={Google Cloud AI Research, Google Research, Google DeepMind, Houston Methodist, Sequome, Fleming Initiative and Imperial College London, Stanford University},
    url={https://storage.googleapis.com/coscientist_paper/ai_coscientist.pdf}
}

@software{ai_coscientist_framework,
    title={AI-CoScientist: A Multi-Agent Framework for Collaborative Scientific Research},
    author={The Swarm Corporation},
    year={2024},
    url={https://github.com/The-Swarm-Corporation/AI-CoScientist}
}
```

## 🔗 Related Work

- [Original Paper](https://storage.googleapis.com/coscientist_paper/ai_coscientist.pdf) - Towards an AI co-scientist
- [Swarms Framework](https://github.com/kyegomez/swarms) - Multi-agent AI orchestration
- [Google Research](https://research.google) - Original research institution

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/The-Swarm-Corporation/AI-CoScientist/issues)
- **Discussions**: [GitHub Discussions](https://github.com/The-Swarm-Corporation/AI-CoScientist/discussions)
- **Email**: kye@swarms.world
- **Discord**: [Join our community](https://discord.gg/swarms-999382051935506503)

## 📝 TODO

- [ ] **Fix state saving**: Improve agent state persistence and resume functionality
- [ ] **Export hypothesis**: Add JSON/CSV export capabilities for generated hypotheses
- [ ] **Improve Elo rating**: Enhance tournament selection algorithm and rating calculations
- [ ] **Implement hypothesis validation**: Add automated testing framework for hypothesis quality
- [ ] **Enhance agent prompts**: Optimize system prompts for better scientific reasoning
- [ ] **Add literature integration**: Connect with arXiv/PubMed APIs for knowledge grounding
- [ ] **Performance optimization**: Implement parallel agent execution and caching
- [ ] **Add visualization**: Create hypothesis evolution and tournament bracket visualizations
- [ ] **Extend model support**: Add support for more LLM providers and local models

---

<p align="center">
  <strong>Built with Swarms for advancing AI-powered scientific research</strong>
</p>
