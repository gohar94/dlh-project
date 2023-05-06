import os
from pathlib import Path
from yamlwidgets import YamlWidgets
from pytimeloop.app import ModelApp, MapperApp
from pytimeloop.accelergy_interface import invoke_accelergy
from ruamel.yaml import YAML
from ruamel.yaml.compat import StringIO

import logging, sys
logger = logging.getLogger('pytimeloop')
formatter = logging.Formatter(
    '[%(levelname)s] %(asctime)s - %(name)s - %(message)s')
handler = logging.StreamHandler(sys.stdout)
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.INFO)

class ConfigRegistry:
    #################################
    # PIM
    #################################
    PIM_DIR            = Path('example_designs/simple_pim/processing-in-memory-design')
    PIM_ARCH           = PIM_DIR / 'arch/system_PIM.yaml'
    PIM_COMPONENTS_DIR = PIM_DIR / 'arch/components'
    PIM_CONSTRAINTS    = PIM_DIR / 'constraints/constraints.yaml'
    PIM_MAPPER         = PIM_DIR / 'mapper/mapper.yaml'
    
    #################################
    # Eyeriss
    #################################
    EYERISS_DIR              = Path('example_designs/eyeriss_like')
    EYERISS_ARCH             = EYERISS_DIR / 'arch/eyeriss_like.yaml'
    EYERISS_COMPONENTS_DIR   = EYERISS_DIR / 'arch/components'
    EYERISS_ARCH_CONSTRAINTS = EYERISS_DIR / 'constraints/eyeriss_like_arch_constraints.yaml'
    EYERISS_MAP_CONSTRAINTS  = EYERISS_DIR / 'constraints/eyeriss_like_map_constraints.yaml'
    EYERISS_MAPPER           = EYERISS_DIR / 'mapper/mapper.yaml'

    #################################
    # Albireo
    #################################
    ALBIREO_DIR                = Path('example_designs/albireo')
    ALBIREO_ARCH               = ALBIREO_DIR / 'arch/system_albireo.yaml'
    ALBIREO_COMPONENTS_DIR     = ALBIREO_DIR / 'arch/components'
    ALBIREO_CONSTRAINTS        = ALBIREO_DIR / 'constraints/constraints.yaml'
    ALBIREO_MAPPER             = ALBIREO_DIR / 'mapper/mapper.yaml'
    ALBIREO_MAPPING_ALEXNET_L1 = ALBIREO_DIR / 'map/map_alexnet_layer1.yaml'
    ALBIREO_MAPPING_ALEXNET_L2 = ALBIREO_DIR / 'map/map_alexnet_layer2.yaml'
    ALBIREO_MAPPING_ALEXNET_L3 = ALBIREO_DIR / 'map/map_alexnet_layer3.yaml'
    ALBIREO_MAPPING_ALEXNET_L4 = ALBIREO_DIR / 'map/map_alexnet_layer4.yaml'
    ALBIREO_MAPPING_ALEXNET_L5 = ALBIREO_DIR / 'map/map_alexnet_layer5.yaml'
    
    #################################
    # Problems
    #################################
    LAYER_SHAPES_DIR = Path('layer_shapes')
    ALEXNET_LAYER1  = LAYER_SHAPES_DIR / 'AlexNet/AlexNet_layer1.yaml'
    ALEXNET_LAYER2  = LAYER_SHAPES_DIR / 'AlexNet/AlexNet_layer2.yaml'
    ALEXNET_LAYER3  = LAYER_SHAPES_DIR / 'AlexNet/AlexNet_layer3.yaml'
    ALEXNET_LAYER4  = LAYER_SHAPES_DIR / 'AlexNet/AlexNet_layer4.yaml'
    ALEXNET_LAYER5  = LAYER_SHAPES_DIR / 'AlexNet/AlexNet_layer5.yaml'

    #################################
    # Debugging
    #################################
    LAYER_SHAPES_DIR = Path('layer_shapes')
    DEBUGGING_LAYER  = LAYER_SHAPES_DIR / 'Debugging/tinylayer.yaml'

def load_config(*paths):
    yaml = YAML(typ='safe')
    yaml.version = (1, 2)
    total = None
    def _collect_yaml(yaml_str, total):
        new_stuff = yaml.load(yaml_str)
        if total is None:
            return new_stuff

        for key, value in new_stuff.items():
            if key == 'compound_components' and key in total:
                total['compound_components']['classes'] += value['classes']
            elif key in total:
                raise RuntimeError(f'overlapping key: {key}')
            else:
                total[key] = value
        return total

    for path in paths:
        if isinstance(path, str):
            total = _collect_yaml(path, total)
            continue
        elif path.is_dir():
            for p in path.glob('*.yaml'):
                with p.open() as f:
                    total = _collect_yaml(f.read(), total)
        else:
            with path.open() as f:
                total = _collect_yaml(f.read(), total)
    return total

def load_config_str(*paths):
    total = ''
    for path in paths:
        if isinstance(path, str):
            return path
        elif path.is_dir():
            for p in path.glob('*.yaml'):
                with p.open() as f:
                    total += f.read() + '\n'
            return total
        else:
            with path.open() as f:
                return f.read()

def get_paths(paths):
    all_paths = []
    for path in paths:
        if path.is_dir():
            for p in path.glob('*.yaml'):
                all_paths.append(str(p))
        else:
            all_paths.append(str(path))
    return all_paths

def dump_str(yaml_dict):
    yaml = YAML(typ='safe')
    yaml.version = (1, 2)
    yaml.default_flow_style = False
    stream = StringIO()
    yaml.dump(yaml_dict, stream)
    return stream.getvalue()

def show_config(*paths):
    print(load_config_str(*paths))

def load_widget_config(*paths, title=''):
    widget = YamlWidgets(load_config_str(*paths), title=title)
    widget.display()
    return widget

def run_timeloop_model(*paths):
    yaml_str = dump_str(load_config(*paths))
    model = ModelApp(yaml_str, '.')
    result = model.run_subprocess()
    return result

def run_accelergy(*paths):
    has_str = False
    for path in paths:
        if isinstance(path, str):
            has_str = True
            break
    if has_str:
        yaml_str = dump_str(load_config(*paths))
        with open('tmp-accelergy.yaml', 'w') as f:
            f.write(yaml_str)
        result = invoke_accelergy(['tmp-accelergy.yaml'], '', '.')
        os.remove('tmp-accelergy.yaml')
    else:
        result = invoke_accelergy(get_paths(paths), '', '.')
    return result

def configure_mapping(config_str, mapping, var):
    config = load_config(config_str)
    for key in var:
        for level in config['options']:
            for level_key in level:
                if key == level_key:
                    var[key] = level[level_key]
    with open(mapping, 'r') as f:
        complete_mapping = eval(f.read())
    return complete_mapping

def run_timeloop_mapper(*paths):
    yaml_str = dump_str(load_config(*paths))
    mapper = MapperApp(yaml_str, '.')
    result = mapper.run_subprocess()
    return result
