from mlc_chat import ChatModule
from mlc_chat.callback import StreamToStdout

def run():
    cm = ChatModule(
        model="/data/models/mlc/dist/Llama-2-7b-chat-hf-q4f16_ft/params",
        model_lib_path="/data/models/mlc/dist/Llama-2-7b-chat-hf-q4f16_ft/Llama-2-7b-chat-hf-q4f16_ft-cuda.so")
    while True:
        prompt = input('\033[94m' +"Prompt: " + '\033[0m')
        cm.generate(
        prompt=prompt,
        progress_callback=StreamToStdout(callback_interval=2),
        )

if __name__ == '__main__':
    run()