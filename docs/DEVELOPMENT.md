# Local development and builds

This document contains technical build and debugging notes for this personal fork. It does not define contribution, review, approval, or project-governance rules.

## Flutter

Use the Flutter SDK version recorded in [`.github/flutter-version`](../.github/flutter-version).

```sh
flutter pub get
flutter gen-l10n
dart run build_runner build --delete-conflicting-outputs
flutter run
```

For an unsigned distribution pipeline, configure platform signing credentials independently. A manually built Android **debug** APK is not a production release.

## eBook rendering (foliate-js)

The rendering code lives under `assets/foliate-js`. The bundled assets are loaded through `lib/service/book_player/book_player_server.dart`; Dart/WebView communication is implemented in `lib/page/book_player/epub_player.dart`.

For browser debugging:

```sh
cd assets/foliate-js
npm install
npm run debug
```

Then visit `http://localhost:3000/debug.html`. Browser developer tools and the controls on that page help exercise pagination. Adjust `mockParams` in `debug.html` to test styles; `getCSS` in `book.js` controls the reader's applied CSS.

To rebuild the JavaScript bundle:

```sh
cd assets/foliate-js
npm install
npm run build
```

The build generates `dist/bundle.js`; run the Flutter app again to verify integration.

## Optional GitHub Actions

- **CI**: analyze and test on pushes, or run manually.
- **Build Android (Manual)**: manually produce a debug APK.
- **Build Windows (Manual)**: manually build a Windows artifact.
- **Build Linux**: manually build Linux packages.

The former automatic release, store publishing, signing, and community-triage automation is intentionally not used in this fork.
