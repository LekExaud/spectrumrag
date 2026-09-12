# SpectrumRAG Engine: Prompt Engineering Notes

This directory houses structured system prompts and chain-of-thought (CoT) templates for parsing telecommunications regulations (ITU-R, TCRA, 3GPP).

## Observations & Improvements

- **Role Prompting**: Explicitly defining the AI as an expert telecommunications regulatory compliance assistant significantly reduced conversational filler and established clear domain authority.
- **Few-Shot Chain-of-Thought (CoT)**: For complex frequency allocations, forcing models through explicit step-by-step reasoning (identifying band regions, checking regional allocations, cross-referencing national plans) minimized hallucinations compared to zero-shot queries.
- **Auditability Constraints**: Requiring explicit citations of standards and allocation types ensures output reliability for regulatory workflows.