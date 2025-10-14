
# Contributing to Shippuden Stories

Thank you for your interest in contributing! 🎉
This project is a **fan-made, non-commercial project** inspired by *Naruto*.
- Do not upload or submit copyrighted or trademarked material you do not own.
- This project is **not affiliated with or endorsed by Masashi Kishimoto, Shueisha, TV Tokyo, or Studio Pierrot**.

## Getting Started

1.  **Fork** the repository.

2.  **Create a new branch** for your feature or fix:

```
git checkout -b feature/replace-sprites
```
3.  **Make your changes** and commit them with clear messages:
```
git commit -m "Replacing Gaara Sprites"
```
4.  **Push** to your fork and open a **Pull Request**:

```
git push origin feature/replace-sprites
```

5. Wait for review and feedback

  

## 🌀How to Write a Story
1. In the storyline folder create a new python file (e.g `kakashis_tale.py`)
2. Use `demo.py` as a guide for how to write it out
3. To test it edit `screens\story.py` to import your `STORY` instead of `storyline.demo.STORY`
	(Though do not include this particular change in your PR)
4. Raise a PR to add your story!

In the near future I (or another contributor!) will add functionality to choose which story to run without changing the import in `story.py`
  

## Help

In order of difficulty
1. WRITE THE STORY! Requires very little technical know-how. Just creativity!
2. Replace Gaara's sprites
3. Adding Sasuke
4. Adding Awakenings
5. Adding Projectiles

## Rules on AI Slop
I've only used LLMs for the "unglamorous" work: unit testing, writing markdowns and issues and coming up with a story. Please refrain from attempting to flood the codebase with AI Slop, that being, AI generated code, sprites or stories that clearly do not match the quality or cohesiveness of the codebase.

## Licensing

By contributing, you agree that your contributions will be licensed under the same terms as the project’s [LICENSE](LICENSE.md).
This project includes copyrighted material from *Naruto* (© Masashi Kishimoto / Shueisha / TV Tokyo / Studio Pierrot).
Your contributions must respect those rights and must not include any commercial usage.

---