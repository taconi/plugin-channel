## Adding your own plugin

Add a name, a short description and the link the repository to the `README.md`.
If you find it necessary add a new topic as `Formattings`.

See the Go plugin as an example.
  ### Formattings
  - [`go`](https://github.com/micro-editor/go-plugin) - Provides `gofmt` and `goimports` support for Go files


And add your own plugin, create a `repo.json` file containing all the metadata information for your plugin. See the Go plugin [repo.json](https://github.com/micro-editor/go-plugin/blob/master/repo.json) file as an example.
Then you can open a pull request which adds the link to that file to the `channel.json` file in this repo. See the Go plugin as an example.
```json
  // Go plugin
  "https://raw.githubusercontent.com/micro-editor/go-plugin/master/repo.json",
```
