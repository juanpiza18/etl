from ..pipeline import Pipeline

def test_pipeline_extract():
    pipeline = Pipeline()
    assert hasattr(pipeline, 'extract')
    assert hasattr(pipeline, 'transform')
    assert hasattr(pipeline, 'load')
