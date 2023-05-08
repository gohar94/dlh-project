import re 
import pickle


def get_numbers_from_summary_eyeriss(string):
    keys = [
        'GLOPs',
        'Utilization', 
        'Cycles', 
        'Energy',
        'EDP(J*cycle)', 
        'Area',
        'Computes',
        'pJ/Compute mac',
        'pJ/Compute psum_spad',
        'pJ/Compute weights_spad',
        'pJ/Compute ifmap_spad',
        'pJ/Compute DummyBuffer',
        'pJ/Compute shared_glb',
        'pJ/Compute DRAM',
        'pJ/Compute DRAM <==> shared_glb',
        'pJ/Compute DummyBuffer <==> ifmap_spad',
        'pJ/Compute ifmap_spad <==> weights_spad',
        'pJ/Compute psum_spad <==> mac',
        'pJ/Compute shared_glb <==> DummyBuffer',
        'pJ/Compute weights_spad <==> psum_spad',
        'pJ/Compute Total',
    ]
    
    patterns = re.findall(r"[:=]\s*[-+]?[.]?[\d]+(?:,\d\d\d)*[\.]?\d*(?:[eE][-+]?\d+)?", string)
    
    numbers = [float(
        re.search(r"[-+]?[.]?[\d]+(?:,\d\d\d)*[\.]?\d*(?:[eE][-+]?\d+)?", pattern).group()
    ) for pattern in patterns]
    
    assert len(keys) == len(numbers)
    
    return dict(zip(keys, numbers))


def get_numbers_from_summary_pim(string):
    keys = [
        'GLOPs',
        'Utilization', 
        'Cycles', 
        'Energy',
        'EDP(J*cycle)', 
        'Area',
        'Computes',
        'pJ/Compute mac',
        'pJ/Compute scratchpad',
        'pJ/Compute dummy_buffer',
        'pJ/Compute shared_glb',
        'pJ/Compute DRAM',
        'pJ/Compute A2D_NoC',
        'pJ/Compute D2A_NoC',
        'pJ/Compute DRAM <==> shared_glb',
        'pJ/Compute dummy_buffer <==> scratchpad',
        'pJ/Compute scratchpad <==> mac',
        'pJ/Compute Total',
    ]
    
    patterns = re.findall(r"[:=]\s*[-+]?[.]?[\d]+(?:,\d\d\d)*[\.]?\d*(?:[eE][-+]?\d+)?", string)
    
    numbers = [float(
        re.search(r"[-+]?[.]?[\d]+(?:,\d\d\d)*[\.]?\d*(?:[eE][-+]?\d+)?", pattern).group()
    ) for pattern in patterns]
    
    assert len(keys) == len(numbers)
    
    return dict(zip(keys, numbers))


def get_numbers_from_summary(string):
    keys = [
        'GLOPs',
        'Utilization', 
        'Cycles', 
        'Energy',
        'EDP(J*cycle)', 
        'Area',
        'Computes',
        'pJ/Compute omacs',
        'pJ/Compute psumBuffer',
        'pJ/Compute plcu_dummy_buffer',
        'pJ/Compute weight_cache',
        'pJ/Compute dummy_buffer',
        'pJ/Compute shared_glb',
        'pJ/Compute DRAM',
        'pJ/Compute A2D_NoC',
        'pJ/Compute D2A_NoC',
        'pJ/Compute DRAM <==> shared_glb',
        'pJ/Compute dummy_buffer <==> weight_cache',
        'pJ/Compute plcu_dummy_buffer <==> psumBuffer',
        'pJ/Compute psumBuffer <==> omacs',
        'pJ/Compute weight_cache <==> plcu_dummy_buffer',
        'pJ/Compute Total',
    ]
    
    patterns = re.findall(r"[:=]\s*[-+]?[.]?[\d]+(?:,\d\d\d)*[\.]?\d*(?:[eE][-+]?\d+)?", string)
    
    numbers = [float(
        re.search(r"[-+]?[.]?[\d]+(?:,\d\d\d)*[\.]?\d*(?:[eE][-+]?\d+)?", pattern).group()
    ) for pattern in patterns]
    
    assert len(keys) == len(numbers)
    
    return dict(zip(keys, numbers))


def save_data(obj, fname):
    with open(fname, 'wb') as file:
        pickle.dump(obj, file)

        
def load_data(fname):
    with open(fname, 'rb') as file:
        return pickle.load(file)
    
    
def extract_numbers(stats_by_layer, fname):
    all_stats = []
    
    for stats in stats_by_layer:
        all_stats.append(get_numbers_from_summary(stats[stats.find("Summary Stats"):]))
        
    save_data(all_stats, fname)
    
    
def save_loop_nests(loop_nests, fname):
    string = ''
    for i, loop in enumerate(loop_nests):
        string += 'Layer {}\n\n'.format(i)
        string += loop
        string += '\n\n\n\n'
    
    with open(fname, 'w') as file:
        file.write(string)