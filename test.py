QLoRA:
Low-Rank Adapters (LoRA):
Fine-tunes small, trainable parameters (adapters) while keeping the main model frozen. This allows efficient adaptation to specific tasks without retraining the entire model.

4-bit Normal Float (NF4) Quantization:
Optimally compresses model weights, significantly minimizing memory usage without compromising precision.

Double Quantization:
Further compresses quantization constants, reducing the need for additional memory and enhancing storage efficiency.

Paged Optimizers:
Ensures efficient memory management by preventing out-of-memory errors, particularly during data spikes.
