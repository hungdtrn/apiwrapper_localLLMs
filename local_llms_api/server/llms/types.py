from typing import List, Optional, Dict, Union
from typing_extensions import TypedDict, NotRequired, Literal


class EmbeddingUsage(TypedDict):
    prompt_tokens: int
    total_tokens: int


class EmbeddingData(TypedDict):
    index: int
    object: str
    embedding: List[float]


class Embedding(TypedDict):
    object: Literal["list"]
    model: str
    data: List[EmbeddingData]
    usage: EmbeddingUsage




class CompletionChoice(TypedDict):
    text: str
    index: int
    logprob: Optional[float]
    finish_reason: Optional[str]


class CompletionUsage(TypedDict):
    prompt_tokens: int
    completion_tokens: List[int]
    total_tokens: List[int]


class CompletionChunk(TypedDict):
    id: str
    object: Literal["text_completion"]
    created: int
    model: str
    choices: List[CompletionChoice]


class Completion(TypedDict):
    id: str
    object: Literal["text_completion"]
    created: int
    model: str
    choices: List[CompletionChoice]
    usage: CompletionUsage


class ChatCompletionMessage(TypedDict):
    role: Union[Literal["assistant"], Literal["user"], Literal["system"]]
    content: str
    user: NotRequired[str]


class ChatCompletionChoice(TypedDict):
    index: int
    message: ChatCompletionMessage
    finish_reason: Optional[str]


class ChatCompletion(TypedDict):
    id: str
    object: Literal["chat.completion"]
    created: int
    model: str
    choices: List[ChatCompletionChoice]
    usage: CompletionUsage


class ChatCompletionChunkDelta(TypedDict):
    role: NotRequired[Literal["assistant"]]
    content: NotRequired[str]


class ChatCompletionChunkChoice(TypedDict):
    index: int
    delta: ChatCompletionChunkDelta
    finish_reason: Optional[str]


class ChatCompletionChunk(TypedDict):
    id: str
    model: str
    object: Literal["chat.completion.chunk"]
    created: int
    choices: List[ChatCompletionChunkChoice]
