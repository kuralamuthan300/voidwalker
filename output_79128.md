# Query Report

**Session:** `qr-66d79128`
**Query:** Compare top 3 Hugging Face text-generation models sorted by likes.
**Generated:** 2026-06-19 01:55:46

---

## 1. Original User Goal

> Compare top 3 Hugging Face text-generation models sorted by likes.


## 2. Planner DAG

**Graph nodes:**

- `n:1` **planner** [complete]  inputs=['USER_QUERY']
- `n:10` **critic** [complete]  inputs=['USER_QUERY', 'n:8']
- `n:11` **planner** [complete]  inputs=['USER_QUERY']
- `n:12` **browser** [complete]  inputs=[]
- `n:13` **distiller** [complete]  inputs=['n:12']
- `n:14` **formatter** [skipped]  inputs=['USER_QUERY', 'n:13']
- `n:15` **critic** [complete]  inputs=['USER_QUERY', 'n:13']
- `n:16` **planner** [complete]  inputs=['USER_QUERY']
- `n:17` **browser** [complete]  inputs=[]
- `n:18` **distiller** [complete]  inputs=['n:17']
- `n:19` **formatter** [skipped]  inputs=['USER_QUERY', 'n:18']
- `n:2` **browser** [complete]  inputs=[]
- `n:20` **critic** [complete]  inputs=['USER_QUERY', 'n:18']
- `n:21` **planner** [complete]  inputs=['USER_QUERY']
- `n:22` **browser** [complete]  inputs=[]
- `n:23` **distiller** [complete]  inputs=['n:22']
- `n:24` **formatter** [skipped]  inputs=['USER_QUERY', 'n:23']
- `n:25` **critic** [complete]  inputs=['USER_QUERY', 'n:23']
- `n:26` **planner** [complete]  inputs=['USER_QUERY']
- `n:27` **browser** [complete]  inputs=[]
- `n:28` **distiller** [complete]  inputs=['n:27']
- `n:29` **formatter** [skipped]  inputs=['USER_QUERY', 'n:28']
- `n:3` **distiller** [complete]  inputs=['n:2']
- `n:30` **critic** [complete]  inputs=['USER_QUERY', 'n:28']
- `n:31` **planner** [complete]  inputs=['USER_QUERY']
- `n:32` **browser** [complete]  inputs=[]
- `n:33` **distiller** [complete]  inputs=['n:32']
- `n:34` **formatter** [skipped]  inputs=['USER_QUERY', 'n:33']
- `n:35` **critic** [complete]  inputs=['USER_QUERY', 'n:33']
- `n:36` **planner** [complete]  inputs=['USER_QUERY']
- `n:37` **browser** [complete]  inputs=[]
- `n:38` **distiller** [complete]  inputs=['n:37']
- `n:39` **formatter** [skipped]  inputs=['USER_QUERY', 'n:38']
- `n:4` **formatter** [skipped]  inputs=['USER_QUERY', 'n:3']
- `n:40` **critic** [complete]  inputs=['USER_QUERY', 'n:38']
- `n:41` **planner** [complete]  inputs=['USER_QUERY']
- `n:42` **browser** [complete]  inputs=[]
- `n:43` **distiller** [complete]  inputs=['n:42']
- `n:44` **formatter** [skipped]  inputs=['USER_QUERY', 'n:43']
- `n:45` **critic** [complete]  inputs=['USER_QUERY', 'n:43']
- `n:46` **planner** [complete]  inputs=['USER_QUERY']
- `n:47` **browser** [complete]  inputs=[]
- `n:48` **distiller** [complete]  inputs=['n:47']
- `n:49` **formatter** [skipped]  inputs=['USER_QUERY', 'n:48']
- `n:5` **critic** [complete]  inputs=['USER_QUERY', 'n:3']
- `n:50` **critic** [complete]  inputs=['USER_QUERY', 'n:48']
- `n:51` **planner** [complete]  inputs=['USER_QUERY']
- `n:52` **browser** [complete]  inputs=[]
- `n:53` **distiller** [complete]  inputs=['n:52']
- `n:54` **formatter** [skipped]  inputs=['USER_QUERY', 'n:53']
- `n:55` **critic** [complete]  inputs=['USER_QUERY', 'n:53']
- `n:56` **planner** [complete]  inputs=['USER_QUERY']
- `n:57` **browser** [complete]  inputs=[]
- `n:58` **distiller** [complete]  inputs=['n:57']
- `n:59` **formatter** [skipped]  inputs=['USER_QUERY', 'n:58']
- `n:6` **planner** [complete]  inputs=['USER_QUERY']
- `n:60` **critic** [complete]  inputs=['USER_QUERY', 'n:58']
- `n:61` **planner** [complete]  inputs=['USER_QUERY']
- `n:62` **browser** [complete]  inputs=[]
- `n:63` **distiller** [complete]  inputs=['n:62']
- `n:64` **formatter** [skipped]  inputs=['USER_QUERY', 'n:63']
- `n:65` **critic** [complete]  inputs=['USER_QUERY', 'n:63']
- `n:66` **planner** [complete]  inputs=['USER_QUERY']
- `n:67` **browser** [complete]  inputs=[]
- `n:68` **distiller** [complete]  inputs=['n:67']
- `n:69` **formatter** [skipped]  inputs=['USER_QUERY', 'n:68']
- `n:7` **browser** [complete]  inputs=[]
- `n:70` **critic** [complete]  inputs=['USER_QUERY', 'n:68']
- `n:71` **planner** [complete]  inputs=['USER_QUERY']
- `n:72` **browser** [complete]  inputs=[]
- `n:73` **distiller** [complete]  inputs=['n:72']
- `n:74` **formatter** [skipped]  inputs=['USER_QUERY', 'n:73']
- `n:75` **critic** [complete]  inputs=['USER_QUERY', 'n:73']
- `n:76` **planner** [pending]  inputs=['USER_QUERY']
- `n:8` **distiller** [complete]  inputs=['n:7']
- `n:9` **formatter** [skipped]  inputs=['USER_QUERY', 'n:8']

**Edges (data flow):**

  n:1 → n:2
  n:2 → n:3
  n:3 → n:5
  n:5 → n:4
  n:6 → n:7
  n:7 → n:8
  n:8 → n:10
  n:10 → n:9
  n:11 → n:12
  n:12 → n:13
  n:13 → n:15
  n:15 → n:14
  n:16 → n:17
  n:17 → n:18
  n:18 → n:20
  n:20 → n:19
  n:21 → n:22
  n:22 → n:23
  n:23 → n:25
  n:25 → n:24
  n:26 → n:27
  n:27 → n:28
  n:28 → n:30
  n:30 → n:29
  n:31 → n:32
  n:32 → n:33
  n:33 → n:35
  n:35 → n:34
  n:36 → n:37
  n:37 → n:38
  n:38 → n:40
  n:40 → n:39
  n:41 → n:42
  n:42 → n:43
  n:43 → n:45
  n:45 → n:44
  n:46 → n:47
  n:47 → n:48
  n:48 → n:50
  n:50 → n:49
  n:51 → n:52
  n:52 → n:53
  n:53 → n:55
  n:55 → n:54
  n:56 → n:57
  n:57 → n:58
  n:58 → n:60
  n:60 → n:59
  n:61 → n:62
  n:62 → n:63
  n:63 → n:65
  n:65 → n:64
  n:66 → n:67
  n:67 → n:68
  n:68 → n:70
  n:70 → n:69
  n:71 → n:72
  n:72 → n:73
  n:73 → n:75
  n:75 → n:74


## 3. Browser Path Chosen

**Node n:2** ✅

- **URL:** `https://huggingface.co/models`
- **Goal:** Filter by Task: Text Generation, Sort by: Most Likes; then extract the names, download counts, and library compatibility for the top 3 model cards.
- **Path (layer chosen):** `a11y`
- **Final URL:** `https://huggingface.co/models?pipeline_tag=text-generation&sort=likes`
- **Turns:** 9

---
**Node n:7** ✅

- **URL:** `https://huggingface.co/models`
- **Goal:** Filter by Tasks=Text Generation, Sort=Most Likes; extract the top 3 model names and their total like counts.
- **Path (layer chosen):** `a11y`
- **Final URL:** `https://huggingface.co/models?pipeline_tag=text-generation&sort=likes`
- **Turns:** 4

---
**Node n:12** ✅

- **URL:** `https://huggingface.co/models`
- **Goal:** Filter Tasks=Text Generation, Sort=Most Likes; extract the names, like counts, and descriptions of the top 3 models.
- **Path (layer chosen):** `a11y`
- **Final URL:** `https://huggingface.co/models?pipeline_tag=text-generation&sort=likes`
- **Turns:** 4

---
**Node n:17** ✅

- **URL:** `https://huggingface.co/models`
- **Goal:** Filter by Task: 'Text Generation', then sort by 'Most likes'. Extract the model name, like count, and a brief description for the top 3 models.
- **Path (layer chosen):** `a11y`
- **Final URL:** `https://huggingface.co/models?pipeline_tag=text-generation&sort=likes`
- **Turns:** 4

---
**Node n:22** ✅

- **URL:** `https://huggingface.co/models`
- **Goal:** Filter by Task=Text Generation, Sort=Most Likes. Extract the top 3 model names and their exact like counts as displayed on the page.
- **Path (layer chosen):** `a11y`
- **Final URL:** `https://huggingface.co/models?pipeline_tag=text-generation&sort=likes`
- **Turns:** 4

---
**Node n:27** ✅

- **URL:** `https://huggingface.co/models`
- **Goal:** Filter by Task: Text Generation, Sort by: Most Likes; extract the names, like counts, and descriptions of the top 3 models.
- **Path (layer chosen):** `a11y`
- **Final URL:** `https://huggingface.co/models?pipeline_tag=text-generation&sort=likes`
- **Turns:** 4

---
**Node n:32** ✅

- **URL:** `https://huggingface.co/models`
- **Goal:** Filter by Tasks=Text Generation, Sort=Most Likes; extract the top 3 model cards including their name, likes count, and parameter count.
- **Path (layer chosen):** `a11y`
- **Final URL:** `https://huggingface.co/models?pipeline_tag=text-generation&sort=likes`
- **Turns:** 4

---
**Node n:37** ✅

- **URL:** `https://huggingface.co/models`
- **Goal:** Filter by Task: 'Text Generation', sort by 'Most Likes', and extract the top 3 model names, their likes, and parameter counts if available.
- **Path (layer chosen):** `a11y`
- **Final URL:** `https://huggingface.co/models?pipeline_tag=text-generation&sort=likes`
- **Turns:** 4

---
**Node n:42** ✅

- **URL:** `https://huggingface.co/models`
- **Goal:** Filter by Task=Text Generation, sort by Most Likes, and extract the names, like counts, and brief descriptions of the top 3 models.
- **Path (layer chosen):** `a11y`
- **Final URL:** `https://huggingface.co/models?pipeline_tag=text-generation&sort=likes`
- **Turns:** 4

---
**Node n:47** ✅

- **URL:** `https://huggingface.co/models`
- **Goal:** Filter by Task=Text Generation, Sort=Most Likes; extract the names, like counts, and parameter counts for the top 3 models.
- **Path (layer chosen):** `a11y`
- **Final URL:** `https://huggingface.co/models?pipeline_tag=text-generation&sort=likes`
- **Turns:** 4

---
**Node n:52** ✅

- **URL:** `https://huggingface.co/models`
- **Goal:** Filter by Task: Text Generation, Sort by: Most Likes. Extract the top 3 model names, their like counts, and a brief description for each.
- **Path (layer chosen):** `a11y`
- **Final URL:** `https://huggingface.co/models?pipeline_tag=text-generation&sort=likes`
- **Turns:** 4

---
**Node n:57** ✅

- **URL:** `https://huggingface.co/models`
- **Goal:** Filter by task 'Text Generation', sort by 'Most likes', and extract the top 3 model names and their current like counts.
- **Path (layer chosen):** `a11y`
- **Final URL:** `https://huggingface.co/models?pipeline_tag=text-generation&sort=likes`
- **Turns:** 4

---
**Node n:62** ✅

- **URL:** `https://huggingface.co/models`
- **Goal:** Filter Tasks=Text Generation, Sort=Most Likes; extract the names, like counts, and descriptions of the top 3 models.
- **Path (layer chosen):** `a11y`
- **Final URL:** `https://huggingface.co/models?pipeline_tag=text-generation&sort=likes`
- **Turns:** 4

---
**Node n:67** ✅

- **URL:** `https://huggingface.co/models`
- **Goal:** Filter by Task: Text Generation, Sort by: Most Likes. Extract the top 3 models including their name, likes count, and a brief description.
- **Path (layer chosen):** `a11y`
- **Final URL:** `https://huggingface.co/models?pipeline_tag=text-generation&sort=likes`
- **Turns:** 4

---
**Node n:72** ✅

- **URL:** `https://huggingface.co/models`
- **Goal:** Filter by Task=Text Generation, Sort=Most Likes; extract the names, parameter counts, and like counts for the top 3 models.
- **Path (layer chosen):** `a11y`
- **Final URL:** `https://huggingface.co/models?pipeline_tag=text-generation&sort=likes`
- **Turns:** 4



## 4. Browser Actions Taken

**Node n:2**

  **Turn 1:** `{'type': 'click', 'mark': 36}`  → _outcome: ok_
  **Turn 2:** `{'type': 'click', 'mark': 80}`  → _outcome: ok_
  **Turn 3:** `{'type': 'click', 'mark': 82}`  → _outcome: ok_
  **Turn 4:** `{'type': 'click', 'mark': 81}`  → _outcome: ok_
  **Turn 5:** `{'type': 'click', 'mark': 3}`  → _outcome: ok_
  **Turn 6:** `{'type': 'click', 'mark': 79}`  → _outcome: ok_
  **Turn 7:** `{'type': 'click', 'mark': 81}`  → _outcome: ok_
  **Turn 8:** `{'type': 'click', 'mark': 36}`  → _outcome: ok_
  **Turn 9:** `{'type': 'done', 'success': True, 'value': '1. Name: deepseek-ai/DeepSeek-R1, Downloads: 6.03M, Libraries: Transformers, PyTorch, GGUF, Safetensors. 2. Name: meta-llama/Meta-Llama-3-8B, Downloads: 1.15M, Libraries: Transformers, PyTorch, Safetensors. 3. Name: meta-llama/Llama-3.1-8B-Instruct, Downloads: 8M (approx), Libraries: Transformers, PyTorch, Safetensors.'}`  → _outcome: done(True)_

---
**Node n:7**

  **Turn 1:** `{'type': 'click', 'mark': 36}`  → _outcome: ok_
  **Turn 2:** `{'type': 'click', 'mark': 80}`  → _outcome: ok_
  **Turn 3:** `{'type': 'click', 'mark': 82}`  → _outcome: ok_
  **Turn 4:** `{'type': 'done', 'success': True, 'value': '1. openai/gpt-oss-20b: 6.05M likes, 2. deepseek-ai/DeepSeek-R1: 6.03M likes, 3. deepseek-ai/DeepSeek-V4-Pro: 2.95M likes'}`  → _outcome: done(True)_

---
**Node n:12**

  **Turn 1:** `{'type': 'click', 'mark': 36}`  → _outcome: ok_
  **Turn 2:** `{'type': 'click', 'mark': 80}`  → _outcome: ok_
  **Turn 3:** `{'type': 'click', 'mark': 82}`  → _outcome: ok_
  **Turn 4:** `{'type': 'done', 'success': True, 'value': '1. Name: deepseek-ai/DeepSeek-R1, Likes: 6.03M, Description: Text Generation • 685B • Updated Mar 27, 2025. 2. Name: openai/gpt-oss-20b, Likes: 6.05M, Description: Text Generation • 22B • Updated Aug 26, 2025. 3. Name: deepseek-ai/DeepSeek-V4-Pro, Likes: 2.95M, Description: Text Generation • 862B • Updated 11 days ago.'}`  → _outcome: done(True)_

---
**Node n:17**

  **Turn 1:** `{'type': 'click', 'mark': 36}`  → _outcome: ok_
  **Turn 2:** `{'type': 'click', 'mark': 80}`  → _outcome: ok_
  **Turn 3:** `{'type': 'click', 'mark': 82}`  → _outcome: ok_
  **Turn 4:** `{'type': 'done', 'success': True, 'value': '1. Model: deepseek-ai/DeepSeek-R1, Likes: 6.03M, Description: Text Generation, 685B parameters. 2. Model: openai/gpt-oss-20b, Likes: 6.05M, Description: Text Generation, 22B parameters. 3. Model: deepseek-ai/DeepSeek-V4-Pro, Likes: 2.95M, Description: Text Generation, 862B parameters.'}`  → _outcome: done(True)_

---
**Node n:22**

  **Turn 1:** `{'type': 'click', 'mark': 36}`  → _outcome: ok_
  **Turn 2:** `{'type': 'click', 'mark': 80}`  → _outcome: ok_
  **Turn 3:** `{'type': 'click', 'mark': 82}`  → _outcome: ok_
  **Turn 4:** `{'type': 'done', 'success': True, 'value': '1. openai/gpt-oss-20b: 6.05M, 2. deepseek-ai/DeepSeek-R1: 6.03M, 3. deepseek-ai/DeepSeek-V4-Pro: 2.95M'}`  → _outcome: done(True)_

---
**Node n:27**

  **Turn 1:** `{'type': 'click', 'mark': 36}`  → _outcome: ok_
  **Turn 2:** `{'type': 'click', 'mark': 80}`  → _outcome: ok_
  **Turn 3:** `{'type': 'click', 'mark': 82}`  → _outcome: ok_
  **Turn 4:** `{'type': 'done', 'success': True, 'value': '1. deepseek-ai/DeepSeek-R1, 6.03M likes, Text Generation; 2. openai/gpt-oss-20b, 6.05M likes, Text Generation; 3. openai/gpt-oss-120b, 3.68M likes, Text Generation'}`  → _outcome: done(True)_

---
**Node n:32**

  **Turn 1:** `{'type': 'click', 'mark': 36}`  → _outcome: ok_
  **Turn 2:** `{'type': 'click', 'mark': 80}`  → _outcome: ok_
  **Turn 3:** `{'type': 'click', 'mark': 82}`  → _outcome: ok_
  **Turn 4:** `{'type': 'done', 'success': True, 'value': '1. Name: deepseek-ai/DeepSeek-R1, Likes: 6.03M, Parameters: 685B; 2. Name: openai/gpt-oss-20b, Likes: 6.05M, Parameters: 22B; 3. Name: deepseek-ai/DeepSeek-V4-Pro, Likes: 2.95M, Parameters: 862B'}`  → _outcome: done(True)_

---
**Node n:37**

  **Turn 1:** `{'type': 'click', 'mark': 36}`  → _outcome: ok_
  **Turn 2:** `{'type': 'click', 'mark': 80}`  → _outcome: ok_
  **Turn 3:** `{'type': 'click', 'mark': 82}`  → _outcome: ok_
  **Turn 4:** `{'type': 'done', 'success': True, 'value': '1. deepseek-ai/DeepSeek-R1: 6.03M likes, 685B parameters. 2. openai/gpt-oss-20b: 6.05M likes, 22B parameters. 3. meta-llama/Meta-Llama-3-8B: 1.15M likes, 8B parameters.'}`  → _outcome: done(True)_

---
**Node n:42**

  **Turn 1:** `{'type': 'click', 'mark': 36}`  → _outcome: ok_
  **Turn 2:** `{'type': 'click', 'mark': 80}`  → _outcome: ok_
  **Turn 3:** `{'type': 'click', 'mark': 82}`  → _outcome: ok_
  **Turn 4:** `{'type': 'done', 'success': True, 'value': '1. openai/gpt-oss-20b: 6.05M likes, Text Generation, 22B parameters. 2. deepseek-ai/DeepSeek-R1: 6.03M likes, Text Generation, 685B parameters. 3. openai/gpt-oss-120b: 3.68M likes, Text Generation, 120B parameters.'}`  → _outcome: done(True)_

---
**Node n:47**

  **Turn 1:** `{'type': 'click', 'mark': 36}`  → _outcome: ok_
  **Turn 2:** `{'type': 'click', 'mark': 80}`  → _outcome: ok_
  **Turn 3:** `{'type': 'click', 'mark': 82}`  → _outcome: ok_
  **Turn 4:** `{'type': 'done', 'success': True, 'value': '1. deepseek-ai/DeepSeek-R1: 6.03M likes, 685B parameters. 2. openai/gpt-oss-20b: 6.05M likes, 22B parameters. 3. meta-llama/Meta-Llama-3-8B: 1.15M likes, 8B parameters.'}`  → _outcome: done(True)_

---
**Node n:52**

  **Turn 1:** `{'type': 'click', 'mark': 36}`  → _outcome: ok_
  **Turn 2:** `{'type': 'click', 'mark': 80}`  → _outcome: ok_
  **Turn 3:** `{'type': 'click', 'mark': 82}`  → _outcome: ok_
  **Turn 4:** `{'type': 'done', 'success': True, 'value': '1. deepseek-ai/DeepSeek-R1: 6.03M likes, Text Generation model. 2. openai/gpt-oss-20b: 6.05M likes, Text Generation model. 3. meta-llama/Meta-Llama-3-8B: 1.15M likes, Text Generation model.'}`  → _outcome: done(True)_

---
**Node n:57**

  **Turn 1:** `{'type': 'click', 'mark': 36}`  → _outcome: ok_
  **Turn 2:** `{'type': 'click', 'mark': 80}`  → _outcome: ok_
  **Turn 3:** `{'type': 'click', 'mark': 82}`  → _outcome: ok_
  **Turn 4:** `{'type': 'done', 'success': True, 'value': '1. openai/gpt-oss-20b: 6.05M, 2. deepseek-ai/DeepSeek-R1: 6.03M, 3. deepseek-ai/DeepSeek-V4-Pro: 2.95M'}`  → _outcome: done(True)_

---
**Node n:62**

  **Turn 1:** `{'type': 'click', 'mark': 36}`  → _outcome: ok_
  **Turn 2:** `{'type': 'click', 'mark': 80}`  → _outcome: ok_
  **Turn 3:** `{'type': 'click', 'mark': 82}`  → _outcome: ok_
  **Turn 4:** `{'type': 'done', 'success': True, 'value': '1. Name: deepseek-ai/DeepSeek-R1, Likes: 6.03M, Description: Text Generation • 685B • Updated Mar 27, 2025. 2. Name: openai/gpt-oss-20b, Likes: 6.05M, Description: Text Generation • 22B • Updated Aug 26, 2025. 3. Name: deepseek-ai/DeepSeek-V4-Pro, Likes: 2.95M, Description: Text Generation • 862B • Updated 11 days ago.'}`  → _outcome: done(True)_

---
**Node n:67**

  **Turn 1:** `{'type': 'click', 'mark': 36}`  → _outcome: ok_
  **Turn 2:** `{'type': 'click', 'mark': 80}`  → _outcome: ok_
  **Turn 3:** `{'type': 'click', 'mark': 82}`  → _outcome: ok_
  **Turn 4:** `{'type': 'done', 'success': True, 'value': '1. deepseek-ai/DeepSeek-R1: 6.03M likes, Text Generation model with 685B parameters. 2. openai/gpt-oss-20b: 6.05M likes, Text Generation model with 22B parameters. 3. deepseek-ai/DeepSeek-V4-Pro: 2.95M likes, Text Generation model with 862B parameters.'}`  → _outcome: done(True)_

---
**Node n:72**

  **Turn 1:** `{'type': 'click', 'mark': 36}`  → _outcome: ok_
  **Turn 2:** `{'type': 'click', 'mark': 80}`  → _outcome: ok_
  **Turn 3:** `{'type': 'click', 'mark': 82}`  → _outcome: ok_
  **Turn 4:** `{'type': 'done', 'success': True, 'value': '1. deepseek-ai/DeepSeek-R1: 685B parameters, 6.03M likes. 2. openai/gpt-oss-20b: 22B parameters, 6.05M likes. 3. deepseek-ai/DeepSeek-V4-Pro: 862B parameters, 2.95M likes.'}`  → _outcome: done(True)_



## 5. Screenshots / Page-State Logs

**Node n:2**


**Run directory: `browser_1781813959`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.8 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.2 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.9 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.1 KB)
- `turn_05_legend.txt` (1.7 KB)
- `turn_05_raw.png` (178.3 KB)
- `turn_06_legend.txt` (2.9 KB)
- `turn_06_raw.png` (353.6 KB)
- `turn_07_legend.txt` (3.1 KB)
- `turn_07_raw.png` (366.5 KB)
- `turn_08_legend.txt` (2.9 KB)
- `turn_08_raw.png` (351.4 KB)
- `turn_09_legend.txt` (2.9 KB)
- `turn_09_raw.png` (354.3 KB)

**Run directory: `browser_1781814004`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.8 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.2 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.9 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.1 KB)

**Run directory: `browser_1781814029`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.7 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.3 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.9 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.1 KB)

**Run directory: `browser_1781814053`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.7 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.3 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.9 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.1 KB)

**Run directory: `browser_1781814078`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.7 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.3 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.9 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.1 KB)

**Run directory: `browser_1781814103`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.7 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.3 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.9 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.1 KB)

**Run directory: `browser_1781814128`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.9 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.3 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.9 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.1 KB)

**Run directory: `browser_1781814152`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.9 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.3 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.9 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.1 KB)

**Run directory: `browser_1781814177`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.9 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.2 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.8 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.0 KB)

**Run directory: `browser_1781814202`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.8 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.2 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.8 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.0 KB)

**Run directory: `browser_1781814227`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.8 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.2 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.8 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.0 KB)

**Run directory: `browser_1781814251`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.8 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.2 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.8 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.0 KB)

**Run directory: `browser_1781814276`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.8 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.2 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.8 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.0 KB)

**Run directory: `browser_1781814300`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.8 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.2 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.8 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.0 KB)

**Run directory: `browser_1781814325`**
**Layer: `a11y`**
- `turn_01_legend.txt` (2.9 KB)
- `turn_01_raw.png` (352.9 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.2 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.8 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.1 KB)

---
**Node n:7**


**Run directory: `browser_1781813959`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.8 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.2 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.9 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.1 KB)
- `turn_05_legend.txt` (1.7 KB)
- `turn_05_raw.png` (178.3 KB)
- `turn_06_legend.txt` (2.9 KB)
- `turn_06_raw.png` (353.6 KB)
- `turn_07_legend.txt` (3.1 KB)
- `turn_07_raw.png` (366.5 KB)
- `turn_08_legend.txt` (2.9 KB)
- `turn_08_raw.png` (351.4 KB)
- `turn_09_legend.txt` (2.9 KB)
- `turn_09_raw.png` (354.3 KB)

**Run directory: `browser_1781814004`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.8 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.2 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.9 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.1 KB)

**Run directory: `browser_1781814029`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.7 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.3 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.9 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.1 KB)

**Run directory: `browser_1781814053`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.7 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.3 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.9 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.1 KB)

**Run directory: `browser_1781814078`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.7 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.3 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.9 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.1 KB)

**Run directory: `browser_1781814103`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.7 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.3 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.9 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.1 KB)

**Run directory: `browser_1781814128`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.9 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.3 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.9 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.1 KB)

**Run directory: `browser_1781814152`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.9 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.3 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.9 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.1 KB)

**Run directory: `browser_1781814177`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.9 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.2 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.8 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.0 KB)

**Run directory: `browser_1781814202`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.8 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.2 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.8 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.0 KB)

**Run directory: `browser_1781814227`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.8 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.2 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.8 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.0 KB)

**Run directory: `browser_1781814251`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.8 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.2 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.8 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.0 KB)

**Run directory: `browser_1781814276`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.8 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.2 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.8 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.0 KB)

**Run directory: `browser_1781814300`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.8 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.2 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.8 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.0 KB)

**Run directory: `browser_1781814325`**
**Layer: `a11y`**
- `turn_01_legend.txt` (2.9 KB)
- `turn_01_raw.png` (352.9 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.2 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.8 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.1 KB)

---
**Node n:12**


**Run directory: `browser_1781813959`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.8 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.2 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.9 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.1 KB)
- `turn_05_legend.txt` (1.7 KB)
- `turn_05_raw.png` (178.3 KB)
- `turn_06_legend.txt` (2.9 KB)
- `turn_06_raw.png` (353.6 KB)
- `turn_07_legend.txt` (3.1 KB)
- `turn_07_raw.png` (366.5 KB)
- `turn_08_legend.txt` (2.9 KB)
- `turn_08_raw.png` (351.4 KB)
- `turn_09_legend.txt` (2.9 KB)
- `turn_09_raw.png` (354.3 KB)

**Run directory: `browser_1781814004`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.8 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.2 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.9 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.1 KB)

**Run directory: `browser_1781814029`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.7 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.3 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.9 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.1 KB)

**Run directory: `browser_1781814053`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.7 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.3 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.9 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.1 KB)

**Run directory: `browser_1781814078`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.7 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.3 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.9 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.1 KB)

**Run directory: `browser_1781814103`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.7 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.3 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.9 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.1 KB)

**Run directory: `browser_1781814128`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.9 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.3 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.9 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.1 KB)

**Run directory: `browser_1781814152`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.9 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.3 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.9 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.1 KB)

**Run directory: `browser_1781814177`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.9 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.2 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.8 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.0 KB)

**Run directory: `browser_1781814202`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.8 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.2 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.8 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.0 KB)

**Run directory: `browser_1781814227`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.8 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.2 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.8 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.0 KB)

**Run directory: `browser_1781814251`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.8 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.2 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.8 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.0 KB)

**Run directory: `browser_1781814276`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.8 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.2 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.8 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.0 KB)

**Run directory: `browser_1781814300`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.8 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.2 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.8 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.0 KB)

**Run directory: `browser_1781814325`**
**Layer: `a11y`**
- `turn_01_legend.txt` (2.9 KB)
- `turn_01_raw.png` (352.9 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.2 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.8 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.1 KB)

---
**Node n:17**


**Run directory: `browser_1781813959`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.8 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.2 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.9 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.1 KB)
- `turn_05_legend.txt` (1.7 KB)
- `turn_05_raw.png` (178.3 KB)
- `turn_06_legend.txt` (2.9 KB)
- `turn_06_raw.png` (353.6 KB)
- `turn_07_legend.txt` (3.1 KB)
- `turn_07_raw.png` (366.5 KB)
- `turn_08_legend.txt` (2.9 KB)
- `turn_08_raw.png` (351.4 KB)
- `turn_09_legend.txt` (2.9 KB)
- `turn_09_raw.png` (354.3 KB)

**Run directory: `browser_1781814004`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.8 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.2 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.9 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.1 KB)

**Run directory: `browser_1781814029`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.7 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.3 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.9 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.1 KB)

**Run directory: `browser_1781814053`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.7 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.3 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.9 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.1 KB)

**Run directory: `browser_1781814078`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.7 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.3 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.9 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.1 KB)

**Run directory: `browser_1781814103`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.7 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.3 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.9 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.1 KB)

**Run directory: `browser_1781814128`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.9 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.3 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.9 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.1 KB)

**Run directory: `browser_1781814152`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.9 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.3 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.9 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.1 KB)

**Run directory: `browser_1781814177`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.9 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.2 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.8 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.0 KB)

**Run directory: `browser_1781814202`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.8 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.2 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.8 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.0 KB)

**Run directory: `browser_1781814227`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.8 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.2 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.8 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.0 KB)

**Run directory: `browser_1781814251`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.8 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.2 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.8 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.0 KB)

**Run directory: `browser_1781814276`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.8 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.2 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.8 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.0 KB)

**Run directory: `browser_1781814300`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.8 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.2 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.8 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.0 KB)

**Run directory: `browser_1781814325`**
**Layer: `a11y`**
- `turn_01_legend.txt` (2.9 KB)
- `turn_01_raw.png` (352.9 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.2 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.8 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.1 KB)

---
**Node n:22**


**Run directory: `browser_1781813959`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.8 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.2 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.9 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.1 KB)
- `turn_05_legend.txt` (1.7 KB)
- `turn_05_raw.png` (178.3 KB)
- `turn_06_legend.txt` (2.9 KB)
- `turn_06_raw.png` (353.6 KB)
- `turn_07_legend.txt` (3.1 KB)
- `turn_07_raw.png` (366.5 KB)
- `turn_08_legend.txt` (2.9 KB)
- `turn_08_raw.png` (351.4 KB)
- `turn_09_legend.txt` (2.9 KB)
- `turn_09_raw.png` (354.3 KB)

**Run directory: `browser_1781814004`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.8 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.2 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.9 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.1 KB)

**Run directory: `browser_1781814029`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.7 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.3 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.9 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.1 KB)

**Run directory: `browser_1781814053`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.7 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.3 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.9 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.1 KB)

**Run directory: `browser_1781814078`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.7 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.3 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.9 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.1 KB)

**Run directory: `browser_1781814103`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.7 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.3 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.9 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.1 KB)

**Run directory: `browser_1781814128`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.9 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.3 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.9 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.1 KB)

**Run directory: `browser_1781814152`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.9 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.3 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.9 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.1 KB)

**Run directory: `browser_1781814177`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.9 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.2 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.8 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.0 KB)

**Run directory: `browser_1781814202`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.8 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.2 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.8 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.0 KB)

**Run directory: `browser_1781814227`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.8 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.2 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.8 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.0 KB)

**Run directory: `browser_1781814251`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.8 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.2 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.8 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.0 KB)

**Run directory: `browser_1781814276`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.8 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.2 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.8 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.0 KB)

**Run directory: `browser_1781814300`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.8 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.2 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.8 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.0 KB)

**Run directory: `browser_1781814325`**
**Layer: `a11y`**
- `turn_01_legend.txt` (2.9 KB)
- `turn_01_raw.png` (352.9 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.2 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.8 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.1 KB)

---
**Node n:27**


**Run directory: `browser_1781813959`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.8 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.2 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.9 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.1 KB)
- `turn_05_legend.txt` (1.7 KB)
- `turn_05_raw.png` (178.3 KB)
- `turn_06_legend.txt` (2.9 KB)
- `turn_06_raw.png` (353.6 KB)
- `turn_07_legend.txt` (3.1 KB)
- `turn_07_raw.png` (366.5 KB)
- `turn_08_legend.txt` (2.9 KB)
- `turn_08_raw.png` (351.4 KB)
- `turn_09_legend.txt` (2.9 KB)
- `turn_09_raw.png` (354.3 KB)

**Run directory: `browser_1781814004`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.8 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.2 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.9 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.1 KB)

**Run directory: `browser_1781814029`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.7 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.3 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.9 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.1 KB)

**Run directory: `browser_1781814053`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.7 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.3 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.9 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.1 KB)

**Run directory: `browser_1781814078`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.7 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.3 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.9 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.1 KB)

**Run directory: `browser_1781814103`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.7 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.3 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.9 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.1 KB)

**Run directory: `browser_1781814128`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.9 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.3 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.9 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.1 KB)

**Run directory: `browser_1781814152`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.9 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.3 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.9 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.1 KB)

**Run directory: `browser_1781814177`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.9 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.2 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.8 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.0 KB)

**Run directory: `browser_1781814202`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.8 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.2 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.8 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.0 KB)

**Run directory: `browser_1781814227`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.8 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.2 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.8 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.0 KB)

**Run directory: `browser_1781814251`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.8 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.2 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.8 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.0 KB)

**Run directory: `browser_1781814276`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.8 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.2 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.8 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.0 KB)

**Run directory: `browser_1781814300`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.8 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.2 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.8 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.0 KB)

**Run directory: `browser_1781814325`**
**Layer: `a11y`**
- `turn_01_legend.txt` (2.9 KB)
- `turn_01_raw.png` (352.9 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.2 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.8 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.1 KB)

---
**Node n:32**


**Run directory: `browser_1781813959`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.8 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.2 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.9 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.1 KB)
- `turn_05_legend.txt` (1.7 KB)
- `turn_05_raw.png` (178.3 KB)
- `turn_06_legend.txt` (2.9 KB)
- `turn_06_raw.png` (353.6 KB)
- `turn_07_legend.txt` (3.1 KB)
- `turn_07_raw.png` (366.5 KB)
- `turn_08_legend.txt` (2.9 KB)
- `turn_08_raw.png` (351.4 KB)
- `turn_09_legend.txt` (2.9 KB)
- `turn_09_raw.png` (354.3 KB)

**Run directory: `browser_1781814004`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.8 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.2 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.9 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.1 KB)

**Run directory: `browser_1781814029`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.7 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.3 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.9 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.1 KB)

**Run directory: `browser_1781814053`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.7 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.3 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.9 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.1 KB)

**Run directory: `browser_1781814078`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.7 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.3 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.9 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.1 KB)

**Run directory: `browser_1781814103`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.7 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.3 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.9 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.1 KB)

**Run directory: `browser_1781814128`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.9 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.3 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.9 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.1 KB)

**Run directory: `browser_1781814152`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.9 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.3 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.9 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.1 KB)

**Run directory: `browser_1781814177`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.9 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.2 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.8 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.0 KB)

**Run directory: `browser_1781814202`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.8 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.2 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.8 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.0 KB)

**Run directory: `browser_1781814227`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.8 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.2 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.8 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.0 KB)

**Run directory: `browser_1781814251`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.8 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.2 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.8 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.0 KB)

**Run directory: `browser_1781814276`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.8 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.2 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.8 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.0 KB)

**Run directory: `browser_1781814300`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.8 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.2 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.8 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.0 KB)

**Run directory: `browser_1781814325`**
**Layer: `a11y`**
- `turn_01_legend.txt` (2.9 KB)
- `turn_01_raw.png` (352.9 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.2 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.8 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.1 KB)

---
**Node n:37**


**Run directory: `browser_1781813959`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.8 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.2 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.9 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.1 KB)
- `turn_05_legend.txt` (1.7 KB)
- `turn_05_raw.png` (178.3 KB)
- `turn_06_legend.txt` (2.9 KB)
- `turn_06_raw.png` (353.6 KB)
- `turn_07_legend.txt` (3.1 KB)
- `turn_07_raw.png` (366.5 KB)
- `turn_08_legend.txt` (2.9 KB)
- `turn_08_raw.png` (351.4 KB)
- `turn_09_legend.txt` (2.9 KB)
- `turn_09_raw.png` (354.3 KB)

**Run directory: `browser_1781814004`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.8 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.2 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.9 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.1 KB)

**Run directory: `browser_1781814029`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.7 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.3 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.9 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.1 KB)

**Run directory: `browser_1781814053`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.7 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.3 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.9 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.1 KB)

**Run directory: `browser_1781814078`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.7 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.3 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.9 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.1 KB)

**Run directory: `browser_1781814103`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.7 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.3 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.9 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.1 KB)

**Run directory: `browser_1781814128`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.9 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.3 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.9 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.1 KB)

**Run directory: `browser_1781814152`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.9 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.3 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.9 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.1 KB)

**Run directory: `browser_1781814177`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.9 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.2 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.8 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.0 KB)

**Run directory: `browser_1781814202`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.8 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.2 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.8 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.0 KB)

**Run directory: `browser_1781814227`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.8 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.2 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.8 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.0 KB)

**Run directory: `browser_1781814251`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.8 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.2 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.8 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.0 KB)

**Run directory: `browser_1781814276`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.8 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.2 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.8 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.0 KB)

**Run directory: `browser_1781814300`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.8 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.2 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.8 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.0 KB)

**Run directory: `browser_1781814325`**
**Layer: `a11y`**
- `turn_01_legend.txt` (2.9 KB)
- `turn_01_raw.png` (352.9 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.2 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.8 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.1 KB)

---
**Node n:42**


**Run directory: `browser_1781813959`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.8 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.2 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.9 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.1 KB)
- `turn_05_legend.txt` (1.7 KB)
- `turn_05_raw.png` (178.3 KB)
- `turn_06_legend.txt` (2.9 KB)
- `turn_06_raw.png` (353.6 KB)
- `turn_07_legend.txt` (3.1 KB)
- `turn_07_raw.png` (366.5 KB)
- `turn_08_legend.txt` (2.9 KB)
- `turn_08_raw.png` (351.4 KB)
- `turn_09_legend.txt` (2.9 KB)
- `turn_09_raw.png` (354.3 KB)

**Run directory: `browser_1781814004`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.8 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.2 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.9 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.1 KB)

**Run directory: `browser_1781814029`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.7 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.3 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.9 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.1 KB)

**Run directory: `browser_1781814053`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.7 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.3 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.9 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.1 KB)

**Run directory: `browser_1781814078`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.7 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.3 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.9 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.1 KB)

**Run directory: `browser_1781814103`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.7 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.3 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.9 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.1 KB)

**Run directory: `browser_1781814128`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.9 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.3 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.9 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.1 KB)

**Run directory: `browser_1781814152`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.9 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.3 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.9 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.1 KB)

**Run directory: `browser_1781814177`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.9 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.2 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.8 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.0 KB)

**Run directory: `browser_1781814202`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.8 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.2 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.8 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.0 KB)

**Run directory: `browser_1781814227`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.8 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.2 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.8 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.0 KB)

**Run directory: `browser_1781814251`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.8 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.2 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.8 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.0 KB)

**Run directory: `browser_1781814276`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.8 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.2 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.8 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.0 KB)

**Run directory: `browser_1781814300`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.8 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.2 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.8 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.0 KB)

**Run directory: `browser_1781814325`**
**Layer: `a11y`**
- `turn_01_legend.txt` (2.9 KB)
- `turn_01_raw.png` (352.9 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.2 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.8 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.1 KB)

---
**Node n:47**


**Run directory: `browser_1781813959`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.8 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.2 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.9 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.1 KB)
- `turn_05_legend.txt` (1.7 KB)
- `turn_05_raw.png` (178.3 KB)
- `turn_06_legend.txt` (2.9 KB)
- `turn_06_raw.png` (353.6 KB)
- `turn_07_legend.txt` (3.1 KB)
- `turn_07_raw.png` (366.5 KB)
- `turn_08_legend.txt` (2.9 KB)
- `turn_08_raw.png` (351.4 KB)
- `turn_09_legend.txt` (2.9 KB)
- `turn_09_raw.png` (354.3 KB)

**Run directory: `browser_1781814004`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.8 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.2 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.9 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.1 KB)

**Run directory: `browser_1781814029`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.7 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.3 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.9 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.1 KB)

**Run directory: `browser_1781814053`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.7 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.3 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.9 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.1 KB)

**Run directory: `browser_1781814078`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.7 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.3 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.9 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.1 KB)

**Run directory: `browser_1781814103`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.7 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.3 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.9 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.1 KB)

**Run directory: `browser_1781814128`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.9 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.3 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.9 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.1 KB)

**Run directory: `browser_1781814152`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.9 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.3 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.9 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.1 KB)

**Run directory: `browser_1781814177`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.9 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.2 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.8 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.0 KB)

**Run directory: `browser_1781814202`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.8 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.2 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.8 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.0 KB)

**Run directory: `browser_1781814227`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.8 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.2 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.8 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.0 KB)

**Run directory: `browser_1781814251`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.8 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.2 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.8 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.0 KB)

**Run directory: `browser_1781814276`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.8 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.2 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.8 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.0 KB)

**Run directory: `browser_1781814300`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.8 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.2 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.8 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.0 KB)

**Run directory: `browser_1781814325`**
**Layer: `a11y`**
- `turn_01_legend.txt` (2.9 KB)
- `turn_01_raw.png` (352.9 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.2 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.8 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.1 KB)

---
**Node n:52**


**Run directory: `browser_1781813959`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.8 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.2 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.9 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.1 KB)
- `turn_05_legend.txt` (1.7 KB)
- `turn_05_raw.png` (178.3 KB)
- `turn_06_legend.txt` (2.9 KB)
- `turn_06_raw.png` (353.6 KB)
- `turn_07_legend.txt` (3.1 KB)
- `turn_07_raw.png` (366.5 KB)
- `turn_08_legend.txt` (2.9 KB)
- `turn_08_raw.png` (351.4 KB)
- `turn_09_legend.txt` (2.9 KB)
- `turn_09_raw.png` (354.3 KB)

**Run directory: `browser_1781814004`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.8 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.2 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.9 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.1 KB)

**Run directory: `browser_1781814029`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.7 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.3 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.9 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.1 KB)

**Run directory: `browser_1781814053`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.7 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.3 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.9 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.1 KB)

**Run directory: `browser_1781814078`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.7 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.3 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.9 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.1 KB)

**Run directory: `browser_1781814103`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.7 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.3 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.9 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.1 KB)

**Run directory: `browser_1781814128`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.9 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.3 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.9 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.1 KB)

**Run directory: `browser_1781814152`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.9 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.3 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.9 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.1 KB)

**Run directory: `browser_1781814177`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.9 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.2 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.8 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.0 KB)

**Run directory: `browser_1781814202`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.8 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.2 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.8 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.0 KB)

**Run directory: `browser_1781814227`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.8 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.2 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.8 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.0 KB)

**Run directory: `browser_1781814251`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.8 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.2 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.8 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.0 KB)

**Run directory: `browser_1781814276`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.8 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.2 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.8 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.0 KB)

**Run directory: `browser_1781814300`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.8 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.2 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.8 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.0 KB)

**Run directory: `browser_1781814325`**
**Layer: `a11y`**
- `turn_01_legend.txt` (2.9 KB)
- `turn_01_raw.png` (352.9 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.2 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.8 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.1 KB)

---
**Node n:57**


**Run directory: `browser_1781813959`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.8 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.2 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.9 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.1 KB)
- `turn_05_legend.txt` (1.7 KB)
- `turn_05_raw.png` (178.3 KB)
- `turn_06_legend.txt` (2.9 KB)
- `turn_06_raw.png` (353.6 KB)
- `turn_07_legend.txt` (3.1 KB)
- `turn_07_raw.png` (366.5 KB)
- `turn_08_legend.txt` (2.9 KB)
- `turn_08_raw.png` (351.4 KB)
- `turn_09_legend.txt` (2.9 KB)
- `turn_09_raw.png` (354.3 KB)

**Run directory: `browser_1781814004`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.8 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.2 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.9 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.1 KB)

**Run directory: `browser_1781814029`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.7 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.3 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.9 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.1 KB)

**Run directory: `browser_1781814053`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.7 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.3 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.9 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.1 KB)

**Run directory: `browser_1781814078`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.7 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.3 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.9 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.1 KB)

**Run directory: `browser_1781814103`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.7 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.3 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.9 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.1 KB)

**Run directory: `browser_1781814128`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.9 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.3 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.9 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.1 KB)

**Run directory: `browser_1781814152`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.9 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.3 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.9 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.1 KB)

**Run directory: `browser_1781814177`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.9 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.2 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.8 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.0 KB)

**Run directory: `browser_1781814202`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.8 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.2 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.8 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.0 KB)

**Run directory: `browser_1781814227`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.8 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.2 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.8 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.0 KB)

**Run directory: `browser_1781814251`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.8 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.2 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.8 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.0 KB)

**Run directory: `browser_1781814276`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.8 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.2 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.8 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.0 KB)

**Run directory: `browser_1781814300`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.8 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.2 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.8 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.0 KB)

**Run directory: `browser_1781814325`**
**Layer: `a11y`**
- `turn_01_legend.txt` (2.9 KB)
- `turn_01_raw.png` (352.9 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.2 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.8 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.1 KB)

---
**Node n:62**


**Run directory: `browser_1781813959`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.8 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.2 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.9 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.1 KB)
- `turn_05_legend.txt` (1.7 KB)
- `turn_05_raw.png` (178.3 KB)
- `turn_06_legend.txt` (2.9 KB)
- `turn_06_raw.png` (353.6 KB)
- `turn_07_legend.txt` (3.1 KB)
- `turn_07_raw.png` (366.5 KB)
- `turn_08_legend.txt` (2.9 KB)
- `turn_08_raw.png` (351.4 KB)
- `turn_09_legend.txt` (2.9 KB)
- `turn_09_raw.png` (354.3 KB)

**Run directory: `browser_1781814004`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.8 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.2 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.9 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.1 KB)

**Run directory: `browser_1781814029`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.7 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.3 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.9 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.1 KB)

**Run directory: `browser_1781814053`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.7 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.3 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.9 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.1 KB)

**Run directory: `browser_1781814078`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.7 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.3 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.9 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.1 KB)

**Run directory: `browser_1781814103`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.7 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.3 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.9 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.1 KB)

**Run directory: `browser_1781814128`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.9 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.3 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.9 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.1 KB)

**Run directory: `browser_1781814152`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.9 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.3 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.9 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.1 KB)

**Run directory: `browser_1781814177`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.9 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.2 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.8 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.0 KB)

**Run directory: `browser_1781814202`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.8 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.2 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.8 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.0 KB)

**Run directory: `browser_1781814227`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.8 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.2 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.8 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.0 KB)

**Run directory: `browser_1781814251`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.8 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.2 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.8 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.0 KB)

**Run directory: `browser_1781814276`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.8 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.2 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.8 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.0 KB)

**Run directory: `browser_1781814300`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.8 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.2 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.8 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.0 KB)

**Run directory: `browser_1781814325`**
**Layer: `a11y`**
- `turn_01_legend.txt` (2.9 KB)
- `turn_01_raw.png` (352.9 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.2 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.8 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.1 KB)

---
**Node n:67**


**Run directory: `browser_1781813959`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.8 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.2 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.9 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.1 KB)
- `turn_05_legend.txt` (1.7 KB)
- `turn_05_raw.png` (178.3 KB)
- `turn_06_legend.txt` (2.9 KB)
- `turn_06_raw.png` (353.6 KB)
- `turn_07_legend.txt` (3.1 KB)
- `turn_07_raw.png` (366.5 KB)
- `turn_08_legend.txt` (2.9 KB)
- `turn_08_raw.png` (351.4 KB)
- `turn_09_legend.txt` (2.9 KB)
- `turn_09_raw.png` (354.3 KB)

**Run directory: `browser_1781814004`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.8 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.2 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.9 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.1 KB)

**Run directory: `browser_1781814029`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.7 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.3 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.9 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.1 KB)

**Run directory: `browser_1781814053`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.7 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.3 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.9 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.1 KB)

**Run directory: `browser_1781814078`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.7 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.3 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.9 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.1 KB)

**Run directory: `browser_1781814103`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.7 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.3 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.9 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.1 KB)

**Run directory: `browser_1781814128`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.9 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.3 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.9 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.1 KB)

**Run directory: `browser_1781814152`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.9 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.3 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.9 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.1 KB)

**Run directory: `browser_1781814177`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.9 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.2 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.8 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.0 KB)

**Run directory: `browser_1781814202`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.8 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.2 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.8 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.0 KB)

**Run directory: `browser_1781814227`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.8 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.2 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.8 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.0 KB)

**Run directory: `browser_1781814251`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.8 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.2 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.8 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.0 KB)

**Run directory: `browser_1781814276`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.8 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.2 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.8 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.0 KB)

**Run directory: `browser_1781814300`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.8 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.2 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.8 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.0 KB)

**Run directory: `browser_1781814325`**
**Layer: `a11y`**
- `turn_01_legend.txt` (2.9 KB)
- `turn_01_raw.png` (352.9 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.2 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.8 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.1 KB)

---
**Node n:72**


**Run directory: `browser_1781813959`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.8 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.2 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.9 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.1 KB)
- `turn_05_legend.txt` (1.7 KB)
- `turn_05_raw.png` (178.3 KB)
- `turn_06_legend.txt` (2.9 KB)
- `turn_06_raw.png` (353.6 KB)
- `turn_07_legend.txt` (3.1 KB)
- `turn_07_raw.png` (366.5 KB)
- `turn_08_legend.txt` (2.9 KB)
- `turn_08_raw.png` (351.4 KB)
- `turn_09_legend.txt` (2.9 KB)
- `turn_09_raw.png` (354.3 KB)

**Run directory: `browser_1781814004`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.8 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.2 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.9 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.1 KB)

**Run directory: `browser_1781814029`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.7 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.3 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.9 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.1 KB)

**Run directory: `browser_1781814053`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.7 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.3 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.9 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.1 KB)

**Run directory: `browser_1781814078`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.7 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.3 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.9 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.1 KB)

**Run directory: `browser_1781814103`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.7 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.3 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.9 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.1 KB)

**Run directory: `browser_1781814128`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.9 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.3 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.9 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.1 KB)

**Run directory: `browser_1781814152`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.9 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.3 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.9 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.1 KB)

**Run directory: `browser_1781814177`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.9 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.2 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.8 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.0 KB)

**Run directory: `browser_1781814202`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.8 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.2 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.8 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.0 KB)

**Run directory: `browser_1781814227`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.8 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.2 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.8 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.0 KB)

**Run directory: `browser_1781814251`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.8 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.2 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.8 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.0 KB)

**Run directory: `browser_1781814276`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.8 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.2 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.8 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.0 KB)

**Run directory: `browser_1781814300`**
**Layer: `a11y`**
- `turn_01_legend.txt` (3.0 KB)
- `turn_01_raw.png` (381.8 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.2 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.8 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.0 KB)

**Run directory: `browser_1781814325`**
**Layer: `a11y`**
- `turn_01_legend.txt` (2.9 KB)
- `turn_01_raw.png` (352.9 KB)
- `turn_02_legend.txt` (2.9 KB)
- `turn_02_raw.png` (354.2 KB)
- `turn_03_legend.txt` (3.1 KB)
- `turn_03_raw.png` (367.8 KB)
- `turn_04_legend.txt` (2.9 KB)
- `turn_04_raw.png` (356.1 KB)



## 6. Extracted Data

**Node n:3 — Distiller**

```json
{
  "top_models": [
    {
      "name": "deepseek-ai/DeepSeek-R1",
      "downloads": "6.03M",
      "libraries": [
        "Transformers",
        "PyTorch",
        "GGUF",
        "Safetensors"
      ]
    },
    {
      "name": "meta-llama/Meta-Llama-3-8B",
      "downloads": "1.15M",
      "libraries": [
        "Transformers",
        "PyTorch",
        "Safetensors"
      ]
    },
    {
      "name": "meta-llama/Llama-3.1-8B-Instruct",
      "downloads": "8M",
      "libraries": [
        "Transformers",
        "PyTorch",
        "Safetensors"
      ]
    }
  ]
}
```

*Rationale: The model names, download counts, and library compatibility were extracted directly from the browser node's final output.*

---
**Node n:8 — Distiller**

```json
{
  "top_models": [
    {
      "name": "openai/gpt-oss-20b",
      "likes": "6.05M"
    },
    {
      "name": "deepseek-ai/DeepSeek-R1",
      "likes": "6.03M"
    },
    {
      "name": "deepseek-ai/DeepSeek-V4-Pro",
      "likes": "2.95M"
    }
  ]
}
```

*Rationale: The top 3 models and their like counts were extracted directly from the final output value provided in the browser node's action history.*

---
**Node n:13 — Distiller**

```json
{
  "top_models": [
    {
      "name": "openai/gpt-oss-20b",
      "likes": "6.05M",
      "description": "Text Generation • 22B • Updated Aug 26, 2025"
    },
    {
      "name": "deepseek-ai/DeepSeek-R1",
      "likes": "6.03M",
      "description": "Text Generation • 685B • Updated Mar 27, 2025"
    },
    {
      "name": "deepseek-ai/DeepSeek-V4-Pro",
      "likes": "2.95M",
      "description": "Text Generation • 862B • Updated 11 days ago"
    }
  ]
}
```

*Rationale: The top 3 models were extracted from the final output provided in the browser node's turn 4 summary.*

---
**Node n:18 — Distiller**

```json
{
  "top_models": [
    {
      "name": "openai/gpt-oss-20b",
      "likes": "6.05M",
      "parameters": "22B"
    },
    {
      "name": "deepseek-ai/DeepSeek-R1",
      "likes": "6.03M",
      "parameters": "685B"
    },
    {
      "name": "deepseek-ai/DeepSeek-V4-Pro",
      "likes": "2.95M",
      "parameters": "862B"
    }
  ]
}
```

*Rationale: The top 3 models were extracted from the browser node's final turn output based on the requested sort order of most likes.*

---
**Node n:23 — Distiller**

```json
{
  "top_models": [
    {
      "name": "openai/gpt-oss-20b",
      "likes": "6.05M"
    },
    {
      "name": "deepseek-ai/DeepSeek-R1",
      "likes": "6.03M"
    },
    {
      "name": "deepseek-ai/DeepSeek-V4-Pro",
      "likes": "2.95M"
    }
  ]
}
```

*Rationale: The top 3 models and their like counts were extracted directly from the final action outcome in the browser node input.*

---
**Node n:28 — Distiller**

```json
{
  "top_models": [
    {
      "name": "deepseek-ai/DeepSeek-R1",
      "likes": "6.03M",
      "description": "Text Generation"
    },
    {
      "name": "openai/gpt-oss-20b",
      "likes": "6.05M",
      "description": "Text Generation"
    },
    {
      "name": "openai/gpt-oss-120b",
      "likes": "3.68M",
      "description": "Text Generation"
    }
  ]
}
```

*Rationale: The top 3 models and their respective like counts and descriptions were extracted from the final outcome provided in the browser node's output.*

---
**Node n:33 — Distiller**

```json
{
  "top_models": [
    {
      "model_name": "openai/gpt-oss-20b",
      "likes": "6.05M",
      "parameter_count": "22B"
    },
    {
      "model_name": "deepseek-ai/DeepSeek-R1",
      "likes": "6.03M",
      "parameter_count": "685B"
    },
    {
      "model_name": "deepseek-ai/DeepSeek-V4-Pro",
      "likes": "2.95M",
      "parameter_count": "862B"
    }
  ]
}
```

*Rationale: The top 3 models were extracted directly from the final output summary provided in the browser node (n:32).*

---
**Node n:38 — Distiller**

```json
{
  "top_models": [
    {
      "name": "deepseek-ai/DeepSeek-R1",
      "likes": "6.03M",
      "parameters": "685B"
    },
    {
      "name": "openai/gpt-oss-20b",
      "likes": "6.05M",
      "parameters": "22B"
    },
    {
      "name": "meta-llama/Meta-Llama-3-8B",
      "likes": "1.15M",
      "parameters": "8B"
    }
  ]
}
```

*Rationale: The data is extracted directly from the final output of the browser node (n:37).*

---
**Node n:43 — Distiller**

```json
{
  "top_models": [
    {
      "name": "openai/gpt-oss-20b",
      "likes": "6.05M",
      "description": "Text Generation, 22B parameters"
    },
    {
      "name": "deepseek-ai/DeepSeek-R1",
      "likes": "6.03M",
      "description": "Text Generation, 685B parameters"
    },
    {
      "name": "openai/gpt-oss-120b",
      "likes": "3.68M",
      "description": "Text Generation, 120B parameters"
    }
  ]
}
```

*Rationale: The top 3 models and their respective like counts and descriptions were extracted from the final output of the browser tool.*

---
**Node n:48 — Distiller**

```json
{
  "top_models": [
    {
      "name": "deepseek-ai/DeepSeek-R1",
      "likes": "6.03M",
      "parameters": "685B"
    },
    {
      "name": "openai/gpt-oss-20b",
      "likes": "6.05M",
      "parameters": "22B"
    },
    {
      "name": "meta-llama/Meta-Llama-3-8B",
      "likes": "1.15M",
      "parameters": "8B"
    }
  ]
}
```

*Rationale: The model names, like counts, and parameter counts were extracted directly from the browser output's final summary.*

---
**Node n:53 — Distiller**

```json
{
  "top_models": [
    {
      "name": "openai/gpt-oss-20b",
      "like_count": "6.05M",
      "description": "Text Generation model"
    },
    {
      "name": "deepseek-ai/DeepSeek-R1",
      "like_count": "6.03M",
      "description": "Text Generation model"
    },
    {
      "name": "meta-llama/Meta-Llama-3-8B",
      "like_count": "1.15M",
      "description": "Text Generation model"
    }
  ]
}
```

*Rationale: The top 3 models were extracted from the final output provided in the browser node's turn 4 summary.*

---
**Node n:58 — Distiller**

```json
{
  "model_1": "openai/gpt-oss-20b",
  "likes_1": "6.05M",
  "model_2": "deepseek-ai/DeepSeek-R1",
  "likes_2": "6.03M",
  "model_3": "deepseek-ai/DeepSeek-V4-Pro",
  "likes_3": "2.95M"
}
```

*Rationale: The top 3 models and their like counts were extracted directly from the final outcome value provided in the browser node output.*

---
**Node n:63 — Distiller**

```json
{
  "top_models": [
    {
      "name": "deepseek-ai/DeepSeek-R1",
      "likes": "6.03M",
      "description": "Text Generation • 685B • Updated Mar 27, 2025"
    },
    {
      "name": "openai/gpt-oss-20b",
      "likes": "6.05M",
      "description": "Text Generation • 22B • Updated Aug 26, 2025"
    },
    {
      "name": "deepseek-ai/DeepSeek-V4-Pro",
      "likes": "2.95M",
      "description": "Text Generation • 862B • Updated 11 days ago"
    }
  ]
}
```

*Rationale: The model names, like counts, and descriptions were extracted directly from the browser output provided in the final turn of the input.*

---
**Node n:68 — Distiller**

```json
{
  "top_models": [
    {
      "name": "openai/gpt-oss-20b",
      "likes": "6.05M",
      "description": "Text Generation model with 22B parameters"
    },
    {
      "name": "deepseek-ai/DeepSeek-R1",
      "likes": "6.03M",
      "description": "Text Generation model with 685B parameters"
    },
    {
      "name": "deepseek-ai/DeepSeek-V4-Pro",
      "likes": "2.95M",
      "description": "Text Generation model with 862B parameters"
    }
  ]
}
```

*Rationale: The top 3 models were extracted from the final output provided in the browser node (n:67).*

---
**Node n:73 — Distiller**

```json
{
  "top_models": [
    {
      "name": "deepseek-ai/DeepSeek-R1",
      "parameters": "685B",
      "likes": "6.03M"
    },
    {
      "name": "openai/gpt-oss-20b",
      "parameters": "22B",
      "likes": "6.05M"
    },
    {
      "name": "deepseek-ai/DeepSeek-V4-Pro",
      "parameters": "862B",
      "likes": "2.95M"
    }
  ]
}
```

*Rationale: The data was extracted directly from the final output summary provided in the browser node (n:72).*



## 7. Final Comparison Table

_(No formatter output available.)_


## 8. Turn Count & Cost Summary

| Node      | Skill              | Status   | Time    | Gateway Ledger (calls / tokens) | Provider      | Turns |
| :-------- | :----------------- | :------- | :------ | :------------------------------- | :------------ | :---- |
| n:1      | planner            | complete |    4.9s | 15 calls                         | gemini       |      |
| n:2      | browser            | complete |   36.9s | 65 calls                         | —            | 9    |
| n:3      | distiller          | complete |    4.1s | 15 calls                         | gemini       |      |
| n:5      | critic             | complete |    0.8s | 15 calls                         | groq         |      |
| n:6      | planner            | complete |    3.7s | 15 calls                         | gemini       |      |
| n:7      | browser            | complete |   16.3s | 65 calls                         | —            | 4    |
| n:8      | distiller          | complete |    3.7s | 15 calls                         | gemini       |      |
| n:10     | critic             | complete |    1.0s | 15 calls                         | groq         |      |
| n:11     | planner            | complete |    3.4s | 15 calls                         | gemini       |      |
| n:12     | browser            | complete |   16.6s | 65 calls                         | —            | 4    |
| n:13     | distiller          | complete |    3.9s | 15 calls                         | gemini       |      |
| n:15     | critic             | complete |    1.7s | 15 calls                         | groq         |      |
| n:16     | planner            | complete |    2.4s | 15 calls                         | gemini       |      |
| n:17     | browser            | complete |   16.3s | 65 calls                         | —            | 4    |
| n:18     | distiller          | complete |    3.6s | 15 calls                         | gemini       |      |
| n:20     | critic             | complete |    1.4s | 15 calls                         | groq         |      |
| n:21     | planner            | complete |    3.2s | 15 calls                         | gemini       |      |
| n:22     | browser            | complete |   16.2s | 65 calls                         | —            | 4    |
| n:23     | distiller          | complete |    3.6s | 15 calls                         | gemini       |      |
| n:25     | critic             | complete |    1.1s | 15 calls                         | groq         |      |
| n:26     | planner            | complete |    3.9s | 15 calls                         | gemini       |      |
| n:27     | browser            | complete |   17.1s | 65 calls                         | —            | 4    |
| n:28     | distiller          | complete |    3.7s | 15 calls                         | gemini       |      |
| n:30     | critic             | complete |    1.1s | 15 calls                         | groq         |      |
| n:31     | planner            | complete |    3.4s | 15 calls                         | gemini       |      |
| n:32     | browser            | complete |   16.4s | 65 calls                         | —            | 4    |
| n:33     | distiller          | complete |    3.5s | 15 calls                         | gemini       |      |
| n:35     | critic             | complete |    1.1s | 15 calls                         | groq         |      |
| n:36     | planner            | complete |    3.5s | 15 calls                         | gemini       |      |
| n:37     | browser            | complete |   16.2s | 65 calls                         | —            | 4    |
| n:38     | distiller          | complete |    3.8s | 15 calls                         | gemini       |      |
| n:40     | critic             | complete |    1.1s | 15 calls                         | groq         |      |
| n:41     | planner            | complete |    3.5s | 15 calls                         | gemini       |      |
| n:42     | browser            | complete |   16.9s | 65 calls                         | —            | 4    |
| n:43     | distiller          | complete |    3.6s | 15 calls                         | gemini       |      |
| n:45     | critic             | complete |    1.6s | 15 calls                         | groq         |      |
| n:46     | planner            | complete |    2.9s | 15 calls                         | gemini       |      |
| n:47     | browser            | complete |   16.4s | 65 calls                         | —            | 4    |
| n:48     | distiller          | complete |    3.5s | 15 calls                         | gemini       |      |
| n:50     | critic             | complete |    1.1s | 15 calls                         | groq         |      |
| n:51     | planner            | complete |    3.6s | 15 calls                         | gemini       |      |
| n:52     | browser            | complete |   16.4s | 65 calls                         | —            | 4    |
| n:53     | distiller          | complete |    3.8s | 15 calls                         | gemini       |      |
| n:55     | critic             | complete |    1.1s | 15 calls                         | groq         |      |
| n:56     | planner            | complete |    3.3s | 15 calls                         | gemini       |      |
| n:57     | browser            | complete |   16.1s | 65 calls                         | —            | 4    |
| n:58     | distiller          | complete |    4.0s | 15 calls                         | gemini       |      |
| n:60     | critic             | complete |    1.5s | 15 calls                         | groq         |      |
| n:61     | planner            | complete |    2.9s | 15 calls                         | gemini       |      |
| n:62     | browser            | complete |   16.4s | 65 calls                         | —            | 4    |
| n:63     | distiller          | complete |    3.9s | 15 calls                         | gemini       |      |
| n:65     | critic             | complete |    1.1s | 15 calls                         | groq         |      |
| n:66     | planner            | complete |    3.1s | 15 calls                         | gemini       |      |
| n:67     | browser            | complete |   16.3s | 65 calls                         | —            | 4    |
| n:68     | distiller          | complete |    4.1s | 15 calls                         | gemini       |      |
| n:70     | critic             | complete |    1.0s | 15 calls                         | groq         |      |
| n:71     | planner            | complete |    3.1s | 15 calls                         | gemini       |      |
| n:72     | browser            | complete |   16.5s | 65 calls                         | —            | 4    |
| n:73     | distiller          | complete |    3.9s | 15 calls                         | gemini       |      |
| n:75     | critic             | complete |    1.1s | 15 calls                         | groq         |      |
| **Total** | **60 nodes** |          | **392.0s** | **$0.076185** |                |       |

