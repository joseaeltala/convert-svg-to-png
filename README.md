# Convert-SVG-to-png @ only
Convert the SVG code inserted in a file (include .svg files) to PNG.

# Inputs
| NAME | VALUE | DEFAULT | DESCRIPTION |
| ---- | ----- | ------- | ----------- |
| file | string | README.md | The file from which the SVG code will be collected and in which the code will be replaced by a call to the generated PNG|
| path | string | Images/ | The path where the PNG file will go |
| name | string | svg | The filename format to save the PNG file |


# Example Workflow file
    on: push
    jobs:
      Makefiles:
        runs-on: ubuntu-latest
        steps:
          - uses: actions/checkout@v1
          - name: convert-svg-to-png
            uses: joseaeltala/convert-svg-to-png/@only
            with:
              file: "README.md"
              path: "Images/png"
              name: "converted-svg-file"
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
