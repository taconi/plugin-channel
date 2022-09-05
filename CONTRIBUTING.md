## Adding your own plugin

And add a name, a short description, the link the repository and mark if is compatible with micro 2.0. See the Go plugin as an example.

| Plugin | Description | Link | 2.0 Support |
| ------ | ----------- | ---- | ----------- |
| `go` | Provides `gofmt` and `goimports` support for Go files | https://github.com/micro-editor/go-plugin | :heavy_check_mark: |

To add your own plugin, create a `repo.json` file containing all the metadata information for your plugin. See the Go plugin [repo.json](https://github.com/micro-editor/go-plugin/blob/master/repo.json) file as an example.
Then you can open a pull request which adds the link to that file to the `channel.json` file in this repo. See the Go plugin as an example.
```json
  // Go plugin
  "https://raw.githubusercontent.com/micro-editor/go-plugin/master/repo.json",
```
