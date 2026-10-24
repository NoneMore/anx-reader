**English** | [简体中文](README_zh.md) | [Türkçe](README_tr.md) | [Русский](README_RU.md)

<br>

<p align="center">
  <img src="./docs/images/Anx-logo.jpg" alt="Anx-logo" width="100" />
</p>
<h1 align="center">Anx Reader</h1>

> **Personal fork:** This repository is maintained for personal development and customization. It is based on [Anx Reader upstream](https://github.com/Anxcye/anx-reader) and is not an official upstream release or support channel.

Anx Reader, a thoughtfully crafted e-book reader for book lovers. Featuring powerful AI capabilities and supporting various e-book formats, it makes reading smarter and more focused. With its modern interface design, we're committed to delivering pure reading pleasure.


![](./docs/images/main.jpg)


| Feature | Details | Status |
| --- | --- | --- |
| Format Support | EPUB/MOBI/AZW3/FB2/TXT/PDF fully supported | ✅ |
| Cross-Platform Sync | Android/iOS/macOS/Windows coverage<br>Sync books, notes, and reading progress via WebDAV | ✅ |
| AI Assistant | Organizes shelves by progress and tone<br>Generates mind maps for deeper understanding<br>On-demand AI dictionary and translation<br>Delivers perspective analysis and summaries | ✅ |
| Custom Reading Experience | Tune letter, line, paragraph, and margin spacing<br>Adjust font size, style, and weight<br>Customize themes, backgrounds, alignment, and styles | ✅ |
| Notes Workspace | Multiple color/style presets<br>Sort by time or chapter with color filters<br>Export to TXT/Markdown/CSV<br>Create shareable, well-designed cards | ✅ |
| Reading Insights | Track reading time<br>View daily/weekly/monthly/yearly stats<br>Visual heatmap reveals reading habits | ✅ |
| Advanced Extras | TTS with multi-voice, speed, tone, and sleep timer controls<br>Full-book translation with side-by-side view<br>Store books in the cloud and download on demand<br>One-tap simplified/traditional Chinese conversion | ✅ |
| OPDS Catalogs | Built-in OPDS support with custom catalog management | 🛠️ In progress |









## Troubleshooting
Refer to the [troubleshooting guide](./docs/troubleshooting.md#English).

### Screenshots
| ![](./docs/images/wide1.png) | ![](./docs/images/wide2.png) |
| :------------------------------: | :----------------------------: |
|   ![](./docs/images/wide3.png)   |  ![](./docs/images/wide4.png)  |
|   ![](./docs/images/wide5.png)   |  ![](./docs/images/wide6.png)  |
|   ![](./docs/images/wide7.png)   |  ![](./docs/images/wide8.png)  |


| ![](./docs/images/mobile1.png) | ![](./docs/images/mobile2.png) | ![](./docs/images/mobile3.png) |
| :----------------------------: | :----------------------------: | :----------------------------: |
| ![](./docs/images/mobile4.png) | ![](./docs/images/mobile5.png) | ![](./docs/images/mobile6.png) |
| ![](./docs/images/mobile7.png) | ![](./docs/images/mobile8.png) | ![](./docs/images/mobile9.png) |

## Building
Want to build Anx Reader from source? Please follow these steps:
- Install [Flutter](https://flutter.dev).
- Clone and enter the project directory.
- Run `flutter pub get`.
- Run `flutter gen-l10n` to generate multi-language files.
- Run `dart run build_runner build --delete-conflicting-outputs` to generate the Riverpod code.
- Run `flutter run` to launch the application.

You may encounter Flutter version incompatibility issues. Please refer to the [Flutter documentation](https://flutter.dev/docs/get-started/install).


More local development notes: [docs/DEVELOPMENT.md](./docs/DEVELOPMENT.md).

## License
This project is licensed under the [MIT License](./LICENSE).

Starting from version 1.1.4, the open source license for the Anx Reader project has been changed from the MIT License to the GNU General Public License version 3 (GPLv3).

After version 1.2.6, the selection and highlight feature has been rewritten, and the open source license has been changed from the GPL-3.0 License to the MIT License. All contributors agree to this change(#116).

## Thanks
[foliate-js](https://github.com/johnfactotum/foliate-js), which is MIT licensed, it used as the ebook renderer. Thanks to the author for providing such a great project.

[foliate](https://github.com/johnfactotum/foliate), which is GPL-3.0 licensed, selection and highlight feature is inspired by this project. But since 1.2.6, the selection and highlight feature has been rewritten.

And many [other open source projects](./pubspec.yaml), thanks to all the authors for their contributions.
