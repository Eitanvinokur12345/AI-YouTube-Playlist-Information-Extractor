---
name: expo-react-native-ios-claude-code
description: "Use when building a monetized iOS app with Claude Code — sets up the full Expo + React Native stack with MCP servers for autonomous testing, payments, and App Store configuration."
---

# Expo + React Native iOS Development with Claude Code

## Overview
A complete iOS app development workflow using Expo and React Native with Claude Code as the AI coding agent. Leverages MCP servers for each platform service so agents can build, test, configure payments, and publish autonomously — no Swift expertise required.

## Key Techniques
- Use React Native via Expo instead of Swift — Claude Code knows React far better
- Connect the Expo MCP server for autonomous iOS simulator testing
- Use RevenueCat + its MCP server for payment configuration without manual dashboard work
- Use App Store Connect MCP for autonomous metadata and submission configuration
- Install Superwall for remote paywall A/B testing post-launch
- Add PostHog to track onboarding and conversion funnels

## How to Apply
1. Set up an Expo project (`npx create-expo-app`) instead of a native Swift/Xcode project
2. Add Expo MCP server to your Claude Code config so agents can test on the iOS simulator
3. Integrate RevenueCat for subscription/IAP and connect its MCP server
4. Add the App Store Connect MCP server to handle metadata and submission
5. Install Superwall to your app and configure paywall variants remotely
6. Add PostHog for user journey analytics from day one

## Examples
- Building a meditation app: Claude Code writes components in React, Expo MCP handles simulator testing, RevenueCat MCP configures subscription tiers, Superwall A/B tests the paywall
- A productivity tool: entire App Store submission pipeline handled by agents via App Store Connect MCP

## Source
Extracted from: [Top 5 tips for vibe coding an iOS app with Claude Code](https://www.youtube.com/watch?v=3MHWYCsHkpE)
Channel: James Goldbach
