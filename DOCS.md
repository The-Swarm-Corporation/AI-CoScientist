# AI-CoScientist Documentation

## Table of Contents

1. [Overview](#overview)
2. [Architecture](#architecture)
3. [Installation](#installation)
4. [Quick Start](#quick-start)
5. [API Reference](#api-reference)
6. [Agent System](#agent-system)
7. [Configuration](#configuration)
8. [Advanced Usage](#advanced-usage)
9. [Examples](#examples)
10. [Troubleshooting](#troubleshooting)

## Overview

AI-CoScientist is a multi-agent framework that implements the "Towards an AI Co-Scientist" methodology for collaborative scientific research. The system uses specialized AI agents to generate, review, rank, and evolve research hypotheses through tournament-based selection and peer review processes.

### Key Features

- **Multi-Agent Architecture**: 8 specialized agents working in coordination
- **Tournament Selection**: Elo rating system for hypothesis ranking
- **Peer Review System**: Comprehensive scientific evaluation
- **Iterative Refinement**: Meta-review guided evolution
- **Diversity Control**: Proximity analysis to maintain hypothesis diversity
- **State Persistence**: Save and resume research workflows
- **Robust Error Handling**: Production-ready fault tolerance

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
pip install ai-coscientist
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

### Basic Usage

```python
from ai_coscientist import AIScientistFramework

# Initialize the framework
ai_coscientist = AIScientistFramework(
    model_name="gpt-4",
    max_iterations=3,
    hypotheses_per_generation=10
)

# Define your research goal
research_goal = "Develop novel approaches for improving reasoning in LLMs"

# Run the research workflow
results = ai_coscientist.run_research_workflow(research_goal)

# Access results
print(f"Generated {len(results['top_ranked_hypotheses'])} hypotheses")
```

### Advanced Configuration

```python
ai_coscientist = AIScientistFramework(
    model_name="claude-3-sonnet",
    max_iterations=5,
    base_path="./research_states",
    verbose=True,
    tournament_size=12,
    hypotheses_per_generation=15,
    evolution_top_k=5
)
```

## API Reference

### AIScientistFramework Class

#### Constructor

```python
AIScientistFramework(
    model_name: str = "gpt-4",
    max_iterations: int = 3,
    base_path: Optional[str] = None,
    verbose: bool = False,
    tournament_size: int = 8,
    hypotheses_per_generation: int = 10,
    evolution_top_k: int = 3
)
```

**Parameters:**
- `model_name`: LLM model to use for all agents
- `max_iterations`: Number of refinement cycles
- `base_path`: Directory for saving agent states
- `verbose`: Enable detailed logging
- `tournament_size`: Number of hypotheses per tournament round
- `hypotheses_per_generation`: Initial hypothesis count
- `evolution_top_k`: Top hypotheses to evolve each iteration

#### Methods

##### `run_research_workflow(research_goal: str) -> WorkflowResult`

Execute the complete research workflow.

**Parameters:**
- `research_goal`: Research objective description

**Returns:**
- `WorkflowResult`: Dictionary containing results and metrics

##### `save_state() -> None`

Save all agent states to disk for resumption.

##### `load_state() -> None`

Load previously saved agent states.

### Hypothesis Class

```python
@dataclass
class Hypothesis:
    text: str
    elo_rating: int = 1200
    reviews: List[HypothesisReview] = field(default_factory=list)
    score: float = 0.0
    similarity_cluster_id: Optional[str] = None
    evolution_history: List[str] = field(default_factory=list)
    generation_timestamp: float = field(default_factory=time.time)
    win_count: int = 0
    loss_count: int = 0
```

#### Methods

##### `update_elo(opponent_elo: int, win: bool, k_factor: int = 32) -> None`

Update Elo rating based on tournament outcome.

##### `to_dict() -> Dict[str, Any]`

Convert hypothesis to dictionary representation.

## Agent System

### Generation Agent

Creates novel research hypotheses based on:
- Research goal analysis
- Scientific literature knowledge
- Novelty and feasibility considerations

**Output Format:**
```json
{
  "hypotheses": [
    {
      "text": "Hypothesis statement",
      "justification": "Scientific rationale"
    }
  ]
}
```

### Reflection Agent

Provides comprehensive peer review with:
- Scientific soundness evaluation (1-5)
- Novelty assessment (1-5)
- Relevance scoring (1-5)
- Testability analysis (1-5)
- Clarity evaluation (1-5)
- Potential impact assessment (1-5)
- Safety/ethical considerations

### Ranking Agent

Orders hypotheses by composite scores considering:
- Review scores across all criteria
- Scientific merit and feasibility
- Consistency across evaluations

### Evolution Agent

Refines hypotheses through:
- Clarity and precision enhancement
- Scientific soundness strengthening
- Novelty amplification
- Testability improvement
- Safety consideration integration

### Meta-Review Agent

Synthesizes insights including:
- Recurring patterns and themes
- Process assessment and recommendations
- Strategic guidance for evolution
- Potential hypothesis connections

### Proximity Agent

Analyzes hypothesis similarity for:
- Semantic clustering
- Redundancy detection
- Diversity assessment
- Synthesis opportunities

### Tournament Agent

Conducts pairwise comparisons evaluating:
- Scientific soundness
- Novelty and originality
- Relevance to research goal
- Testability and feasibility
- Clarity and precision
- Potential impact

### Supervisor Agent

Orchestrates workflow through:
- Research goal analysis
- Phase-specific planning
- Resource allocation
- Quality control
- Performance optimization

## Configuration

### Environment Variables

```bash
# LLM Provider APIs
OPENAI_API_KEY=your_key
ANTHROPIC_API_KEY=your_key
GOOGLE_API_KEY=your_key

# Logging Configuration
LOG_LEVEL=INFO
LOG_ROTATION=daily
LOG_RETENTION=30d
```

### Model Selection

Supported models:
- `gpt-4`, `gpt-4-turbo`, `gpt-3.5-turbo` (OpenAI)
- `claude-3-opus`, `claude-3-sonnet`, `claude-3-haiku` (Anthropic)
- `gemini-pro`, `gemini-1.5-pro` (Google)

### Tournament Parameters

```python
# Elo rating system
K_FACTOR = 32  # Rating change magnitude
INITIAL_RATING = 1200  # Starting Elo rating

# Tournament configuration
ROUNDS_PER_HYPOTHESIS = 3  # Average matches per hypothesis
MIN_PARTICIPANTS = 2  # Minimum for tournament
```

## Advanced Usage

### Custom Agent Prompts

```python
# Modify agent behavior through prompt customization
framework = AIScientistFramework()
framework.generation_agent.system_prompt = custom_generation_prompt
```

### State Management

```python
# Save research progress
framework.save_state()

# Resume from checkpoint
framework.load_state()

# Custom state directory
framework = AIScientistFramework(base_path="./custom_states")
```

### Metrics and Analysis

```python
results = framework.run_research_workflow(goal)

# Execution metrics
metrics = results['execution_metrics']
print(f"Total time: {metrics['total_time']:.2f}s")
print(f"Agent timings: {metrics['agent_execution_times']}")

# Hypothesis analysis
for hypothesis in results['top_ranked_hypotheses']:
    print(f"Elo: {hypothesis['elo_rating']}")
    print(f"Win rate: {hypothesis['win_rate']}%")
    print(f"Evolution history: {hypothesis['evolution_history']}")
```

### Batch Processing

```python
research_goals = [
    "Novel approaches to AI alignment",
    "Improving LLM factual accuracy",
    "Reducing computational costs in training"
]

results = []
for goal in research_goals:
    result = framework.run_research_workflow(goal)
    results.append(result)
    framework.save_state()  # Checkpoint after each goal
```

## Examples

### Example 1: Machine Learning Research

```python
from ai_coscientist import AIScientistFramework

# Configure for ML research
ai_coscientist = AIScientistFramework(
    model_name="gpt-4",
    max_iterations=4,
    hypotheses_per_generation=12,
    evolution_top_k=4,
    verbose=True
)

# Research goal
goal = "Develop novel architectures for few-shot learning in neural networks"

# Run workflow
results = ai_coscientist.run_research_workflow(goal)

# Analyze top hypotheses
for i, hyp in enumerate(results['top_ranked_hypotheses'][:5], 1):
    print(f"\n{i}. {hyp['text']}")
    print(f"   Elo Rating: {hyp['elo_rating']}")
    print(f"   Scientific Score: {hyp['score']:.2f}")
    
    # Get latest review
    if hyp['reviews']:
        review = hyp['reviews'][-1]
        print(f"   Novelty: {review['scores']['novelty']}/5")
        print(f"   Testability: {review['scores']['testability']}/5")
```

### Example 2: Interdisciplinary Research

```python
# Configure for interdisciplinary research
ai_coscientist = AIScientistFramework(
    model_name="claude-3-sonnet",
    max_iterations=3,
    tournament_size=10,
    hypotheses_per_generation=15
)

# Cross-domain research goal
goal = "Integrate quantum computing principles with machine learning optimization"

results = ai_coscientist.run_research_workflow(goal)

# Examine meta-review insights
insights = results['meta_review_insights']
print("Strategic Recommendations:")
for rec in insights.get('strategic_recommendations', []):
    print(f"- {rec['recommendation']}")
    print(f"  Focus: {rec['focus_area']}")
    print(f"  Justification: {rec['justification']}\n")
```

### Example 3: Hypothesis Evolution Tracking

```python
# Track hypothesis evolution over iterations
ai_coscientist = AIScientistFramework(
    max_iterations=5,
    evolution_top_k=3,
    verbose=True
)

goal = "Novel approaches to explainable AI in deep learning"
results = ai_coscientist.run_research_workflow(goal)

# Analyze evolution history
for hyp in results['top_ranked_hypotheses']:
    if hyp['evolution_history']:
        print(f"Hypothesis: {hyp['text'][:100]}...")
        print("Evolution History:")
        for i, evolution in enumerate(hyp['evolution_history'], 1):
            print(f"  {i}. {evolution}")
        print(f"Final Elo: {hyp['elo_rating']}\n")
```

## Troubleshooting

### Common Issues

#### 1. API Rate Limits

**Problem**: `RateLimitError` from LLM providers

**Solution**: 
```python
import time

# Add delays between agent calls
ai_coscientist = AIScientistFramework()
# The framework includes built-in retry logic
```

#### 2. Empty Agent Responses

**Problem**: Agents returning empty or malformed responses

**Solution**: The framework includes automatic fallbacks, but you can also:
```python
# Enable verbose logging to diagnose
ai_coscientist = AIScientistFramework(verbose=True)

# Check conversation history
results = ai_coscientist.run_research_workflow(goal)
print(results['conversation_history'])
```

#### 3. Memory Issues

**Problem**: Large state files or memory usage

**Solution**:
```python
# Use smaller configurations
ai_coscientist = AIScientistFramework(
    max_iterations=2,
    hypotheses_per_generation=5,
    tournament_size=4
)

# Regular state cleanup
import shutil
shutil.rmtree("./ai_coscientist_states/old_sessions")
```

#### 4. Invalid JSON Responses

**Problem**: Agents returning non-JSON formatted responses

**Solution**: The framework includes robust JSON parsing with multiple fallback strategies. Check logs for details:

```python
# The _safely_parse_json method handles:
# - Markdown code fences
# - Partial JSON responses
# - Malformed JSON with regex extraction
```

### Performance Optimization

#### 1. Model Selection

- Use `gpt-3.5-turbo` for faster, cost-effective research
- Use `gpt-4` for higher quality hypothesis generation
- Use `claude-3-haiku` for rapid iteration phases

#### 2. Parameter Tuning

```python
# For quick prototyping
ai_coscientist = AIScientistFramework(
    max_iterations=1,
    hypotheses_per_generation=5,
    tournament_size=4
)

# For thorough research
ai_coscientist = AIScientistFramework(
    max_iterations=5,
    hypotheses_per_generation=20,
    tournament_size=12,
    evolution_top_k=8
)
```

#### 3. Parallel Processing

The framework runs agents sequentially for consistency. For parallel execution:

```python
# Run multiple research goals concurrently
import concurrent.futures

def run_research(goal):
    framework = AIScientistFramework()
    return framework.run_research_workflow(goal)

goals = ["Goal 1", "Goal 2", "Goal 3"]

with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
    results = list(executor.map(run_research, goals))
```

### Debugging Tips

1. **Enable Verbose Logging**:
   ```python
   ai_coscientist = AIScientistFramework(verbose=True)
   ```

2. **Check Agent States**:
   ```python
   # Inspect saved states
   import json
   with open("./ai_coscientist_states/generation_agent_state.json") as f:
       state = json.load(f)
       print(state)
   ```

3. **Monitor Execution Metrics**:
   ```python
   results = ai_coscientist.run_research_workflow(goal)
   metrics = results['execution_metrics']
   
   # Check for bottlenecks
   for agent, timing in metrics['agent_execution_times'].items():
       print(f"{agent}: {timing['avg_time']:.2f}s average")
   ```

4. **Validate Input Data**:
   ```python
   # Ensure research goal is well-formed
   assert isinstance(research_goal, str)
   assert len(research_goal.strip()) > 10
   assert research_goal.strip() != ""
   ```

## Citation

If you use AI-CoScientist in your research, please cite both the original paper and this software implementation:

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

For additional support, visit our [GitHub Issues](https://github.com/The-Swarm-Corporation/AI-CoScientist/issues) or join our [Discord community](https://discord.gg/swarms-999382051935506503).
