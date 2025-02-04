# StyleGAN-NADA: CLIP-Guided Domain Adaptation of Image Generators (re-implementation)

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/nikita-resh/StyleGAN-NADA/blob/main/colab-notebook.ipynb)

> This repository is a re-implementation of the [paper](https://arxiv.org/abs/2108.00946).
> Here you can find [official implementation](https://github.com/rinongal/StyleGAN-nada).

> StyleGAN-NADA is a method for zero-shot image synthesis editing using text descriptions without requiring labeled datasets or retraining. It modifies a pre-trained StyleGAN model by leveraging CLIP (Contrastive Language-Image Pretraining) to guide the generator toward the desired transformation. The approach uses a latent offset optimization strategy to shift generated images in the latent space based on textual prompts. This enables flexible and efficient style modifications, such as turning portraits into sketches or transforming objects into different artistic styles. StyleGAN-NADA achieves high-quality edits while preserving fine details, making it useful for creative AI applications.

## Key idea

The key idea of the approach is to use two pre-trained generators: one frozen and one trainable. First, the difference vector between the input and target prompts is found in CLIP space. Then, the method seeks a corresponding transformation vector in the W+ space of StyleGAN. Since the generator itself is optimized (rather than individual latent vectors), after training, it can endlessly sample images in the target domain. This enables flexible zero-shot style transformations without requiring labeled datasets or retraining from scratch.

![Main idea](https://raw.githubusercontent.com/nikita-resh/StyleGAN-NADA/refs/heads/main/images/main.png)

## Generator Domain Adaptation

Here are couple of examples of domain adaptation

![Pixar](https://raw.githubusercontent.com/nikita-resh/StyleGAN-NADA/refs/heads/main/images/pixar.png)

_Photo -> Pixar Cartoon_

![Zombie](https://raw.githubusercontent.com/nikita-resh/StyleGAN-NADA/refs/heads/main/images/zombie.png)

_Photo -> Zombie_

![Picasso](https://raw.githubusercontent.com/nikita-resh/StyleGAN-NADA/refs/heads/main/images/picasso.png)
_Photo -> Picasso_

## Pre-requisites

- Main:
  - [Installed CLIP](https://github.com/openai/CLIP)
  - [StyleGan2 (pytorch)](https://github.com/rosinality/stylegan2-pytorch)
  - [Weights for StyleGan2 (pytorch)](https://drive.google.com/uc?id=1EM87UquaoQmk17Q8d5kYIAHqu0dkYqdT)
- For inversion:
  - [e4e](https://github.com/omertov/encoder4editing.git)
  - [Weights for e4e](https://drive.google.com/uc?id=1cUv_reLE6k3604or78EranS7XzuVMWeO)

You can find more details in colab notebook

## Usage

At the moment there is only one possible option to run the work [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/nikita-resh/StyleGAN-NADA/blob/main/colab-notebook.ipynb)
You can just click `Runtime > Run all`, no other actions required.

## Report

[Here you can find the work report](https://github.com/nikita-resh/StyleGAN-NADA/blob/main/REPORT.md)

## Citation

```
@misc{gal2021stylegannada,
      title={StyleGAN-NADA: CLIP-Guided Domain Adaptation of Image Generators},
      author={Rinon Gal and Or Patashnik and Haggai Maron and Gal Chechik and Daniel Cohen-Or},
      year={2021},
      eprint={2108.00946},
      archivePrefix={arXiv},
      primaryClass={cs.CV}
}
```
