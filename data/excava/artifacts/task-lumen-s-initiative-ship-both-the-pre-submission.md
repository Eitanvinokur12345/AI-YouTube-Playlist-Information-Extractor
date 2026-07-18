# [Lumen's initiative] Ship both the pre-submission contrast validator behind a feature flag and the live contrast checker with a non-blocking,

> visualization · task `lumen-s-initiative-ship--44187` · **EXECUTION PLAN — NOT yet executed** · by mistral/mistral-small-latest

```markdown
**Approach:**
Ship both contrast validators behind a feature flag with the pre-submission validator non-blocking and the live checker non-blocking, ensuring backward compatibility.

**Steps:**
1. **Add feature flag** in `src/config/features.ts`:
   ```ts
   export const FEATURE_FLAG_CONTRAST_CHECKER = process.env.FEATURE_FLAG_CONTRAST_CHECKER === 'true';
   ```
2. **Modify pre-submission validator** in `src/validators/contrast.ts`:
   - Wrap validation logic in `if (FEATURE_FLAG_CONTRAST_CHECKER) { ... }`.
   - Log warnings instead of blocking if flag is `false`.
3. **Update live contrast checker** in `src/components/ContrastChecker.tsx`:
   - Use `FEATURE_FLAG_CONTRAST_CHECKER` to conditionally render.
   - Ensure non-blocking UI (e.g., tooltip or passive indicator).
4. **Add flag toggle** in `src/admin/FeatureFlags.tsx`:
   ```tsx
   <Toggle checked={FEATURE_FLAG_CONTRAST_CHECKER} onChange={(v) => setEnv('FEATURE_FLAG_CONTRAST_CHECKER', v)} />
   ```
5. **Deploy to staging** and verify:
   ```sh
   npm run build && npm run deploy:staging
   ```

**Needs:**
- Access to `src/config/features.ts`, `src/validators/contrast.ts`, `src/components/ContrastChecker.tsx`.
- Admin panel permissions for `src/admin/FeatureFlags.tsx`.
- CI/CD pipeline for `npm run deploy:staging`.
- Environment variable `FEATURE_FLAG_CONTRAST_CHECKER` in staging/prod.
```
