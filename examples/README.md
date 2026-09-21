# Examples

## What a step looks like

**Text produced:**

> Click **① Download all (19.27 GB)** — right panel, below the list of three files.
>
> 1. Check the red frames have disappeared around "Load Diffusion Model" and "Load CLIP"
>    → that is the signal the files are in place
> 2. Click **② Run** (blue button, top)
> 3. Wait. First run: 3 to 8 minutes, because 19 GB of models load in chunks
>
> If it fails with `CUDA out of memory`: your VRAM is saturated. Fix: in the **EmptySD3LatentImage** node, set width and height from 1024 to 768, then run again.

**Image produced:** the same panel, cropped, with ① on the download button and ② on the run button, arrows pointing at each, and a blur over anything identifying.

Note what the text does *not* do: it never says "you will see a panel on the right with three files listed". The image already says that.

## Building one

```python
import sys; sys.path.insert(0, "../scripts")
from annotate import Annot

(Annot("raw/comfyui-errors.png")
    .blur(40, 60, 1380, 24)              # bookmarks bar
    .frame(986, 560, 448, 40)            # the target
    .point_at(986, 580, 1)
    .frame(700, 130, 130, 40, color="#2ea043")
    .point_at(700, 150, 2, color="#2ea043")
    .crop_around(1000, 400, 1200, 700)
    .save("out/comfyui-01-download.png"))
```

## Naming

```
<product>-<flow>-<NN>-<slug>.png
```

Two-digit numbers so alphabetical sort matches step order:

```
clustraly-signup-01-open-form.png
clustraly-signup-02-fill-email.png
clustraly-signup-03-validation-error.png
```

That third file is the one most tutorials are missing.
