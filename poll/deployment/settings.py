DEPLOYMENT_STAGE = "development"
stage_settings = __import__( DEPLOYMENT_STAGE, globals(), locals())
globals().update(stage_settings.__dict__)
