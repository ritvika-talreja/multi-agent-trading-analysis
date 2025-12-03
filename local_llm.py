from llama_cpp import Llama

class LocalLLM:
    def __init__(self, model_path: str):
        self.model = Llama(
            model_path=model_path,
            n_ctx=4096,
            n_threads=6,          # Adjust based on CPU
            n_gpu_layers=0,       # CPU mode
            verbose=False
        )

    def call(self, prompt: str):
        output = self.model(
            prompt,
            max_tokens=512,
            temperature=0.7,
            stop=["</s>"]
        )
        return output["choices"][0]["text"].strip()
