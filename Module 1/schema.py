from pydantic import BaseModel, Field
class TextRequest(BaseModel):
    topic: str = Field(
        ...,
        description="The topic for which the text is requested.",
        example="Neural Networks"
    )
    course: str = Field(
        ...,
        description="The course related to the topic.",
        example="Artificial Intelligence"
    )
    student_level: str = Field(
        ...,
        description="The educational level of the student.",
        example="beginner"
    )

# Fifth Function: Code Explainer
class CodeExplainRequest(BaseModel):
    code: str = Field(
        ...,
        min_length=1,
        max_length=20000,
        description="The source code submitted by the student.",
        example="print('Hello World')"
    )
    language: str = Field(
        ...,
        description="Programming language of the submitted code.",
        example="Python"
    )