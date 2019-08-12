from databuri import configuration


def test_read_config():
    config = configuration.read_config(
        additional_configs=['./tests/data/sample.ini']
    )
    assert config.get('main', 'name') == 'databuri'
    assert config.get('main', 'organization') == 'codeforthailand'

    config2 = configuration.read_config(
        additional_configs=[
            './tests/data/sample.ini',
            './tests/data/sample_with_govspending.ini'
        ]
    )
    assert config2.get('main', 'name') == 'databuri'
    assert config2.get('govspending', 'user_token') == 'gov-spending-token'
