import os, json
from fixtures.myapp.sample import save_dict

def test_save_dict(tmpdir ,capsys):
    filepath =os.path.join(tmpdir, 'sample.json')  # to save it as a json file
    _dict= {"a": 1 ,"b": 2}
    save_dict(_dict, filepath)
    assert json.load(open(filepath, 'r')) == _dict
    assert capsys.readouterr().out == "saved\n"