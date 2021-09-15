# Convert-SVG-to-png
Convert SVG code to png and replace the code with a called to the image file in Markdown files

# Objectives
GitHub cannot view SVG files or code from the web, so the main objective of this action is to convert the svg code inserted into any file to PNG, replacing the SVG line by a call to the image (only markdown).

This will be useful to be able to see the SVG code inserted in .MD files from the GitHub web platform.

# Inputs
| NAME | VALUE | DEFAULT | DESCRIPTION |
| ---- | ----- | ------- | ----------- |
| file | string | README.md | The file from which the SVG code will be collected and in which the code will be replaced by a call to the generated PNG|

# Example Workflow file
    on: push
    jobs:
      Makefiles:
        runs-on: ubuntu-latest
        steps:
          - uses: actions/checkout@v1
          - name: convert-svg-to-png
            uses: joseaeltala/convert-svg-to-png/@master
            with:
              file: "README.md"
          - name: Commit files
            run: |
              git config user.name github-actions
              git config user.email github-actions@github.com
              git commit -m "SVG code converted to png" -a
          - name: Push changes
            uses: ad-m/github-push-action@master
            with:
              github_token: ${{ secrets.GITHUB_TOKEN }}
              branch: ${{ github.ref }}
