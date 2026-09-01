# Prompt Used

> Build a GitHub-ready **simple LLM and chatbot** project that can fit on a typical laptop GPU.
>
> Follow the **CRISP-DM framework**:
> 1. Business Understanding
> 2. Data Understanding
> 3. Data Preparation
> 4. Modeling
> 5. Evaluation
> 6. Deployment / Monitoring
>
> Implement a small decoder-only Transformer from scratch using modern LLM primitives while keeping it understandable and lightweight:
> - RoPE rotary position embeddings
> - RMSNorm
> - SwiGLU
> - Grouped-Query Attention
> - optimized scaled-dot-product causal attention
> - residual pre-normalization
> - tied embedding / LM-head weights
>
> Use a small BPE tokenizer and train on a capped stream of TinyStories so the experiment can run on laptop hardware.
>
> Include a practical training loop with:
> - AdamW
> - cosine learning-rate schedule
> - warmup
> - mixed precision when CUDA is available
> - gradient clipping
> - gradient accumulation
> - validation loss
> - perplexity
>
> Include generation using:
> - temperature
> - top-k
> - nucleus/top-p sampling
> - repetition penalty
>
> Turn the model into a simple chatbot using a `User: ... / Assistant:` prompt template and an interactive CLI loop.
>
> Include a polished **Data Science / LLM Admin Dashboard** and a **Chatbot Dashboard**.
>
> Be explicit that a tiny TinyStories model is educational and not a production-quality factual assistant.
>
> Keep GitHub minimal. Include only:
> - one Jupyter notebook
> - README.md
> - prompt_used.md
> - images/
>
> Validate the architecture with a forward and backward pass, but do not fabricate full training metrics if the complete TinyStories training run is not executed in the current environment.
