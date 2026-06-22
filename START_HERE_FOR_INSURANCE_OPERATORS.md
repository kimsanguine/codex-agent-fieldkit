# 보험/서비스 운영자는 여기부터

이 문서는 보험 또는 서비스 운영자가 실제 고객 데이터를 넣기 전에 30분 안에
안전한 연습 루프를 돌리는 경로입니다.

사용하는 데이터는 모두 `ACME Life`라는 가상 회사의 합성 예시입니다.

## 30분 루프

| 시간 | 할 일 | 파일 |
|---:|---|---|
| 0-5분 | public-safe 경계 확인 | [`DATA_POLICY.md`](DATA_POLICY.md) |
| 5-10분 | repo root에서 데모 실행 | `make demo` |
| 10-15분 | 전체 검증 실행 | `make validate` |
| 15-22분 | 보험 합성 pack 읽기 | [`examples/insurance-ops-pack/`](examples/insurance-ops-pack/) |
| 22-27분 | eval/golden-set 구조 확인 | [`examples/insurance-ops-pack/tests/golden_set.jsonl`](examples/insurance-ops-pack/tests/golden_set.jsonl) |
| 27-30분 | validation log와 handoff 작성 방식 확인 | [`examples/insurance-ops-pack/docs/validation_log.md`](examples/insurance-ops-pack/docs/validation_log.md) |

## Codex에게 줄 첫 요청

```text
README.md, AGENTS.md, START_HERE_FOR_INSURANCE_OPERATORS.md,
docs/adapt-for-insurance-ops.md, examples/insurance-ops-pack/README.md를 읽어 주세요.

나는 보험 서비스 운영자입니다. 실제 고객 데이터 없이 ACME Life 합성 데이터로
어떤 질문은 답하고, 어떤 질문은 멈추고, 어떤 질문은 담당자에게 넘겨야 하는지
설명해 주세요.

아직 파일은 수정하지 마세요.
```

## 절대 넣지 않을 것

- 실제 고객명, 연락처, 주소, 계좌, 증권번호
- 실제 청구 서류, 상담 기록, 민원 기록
- 실제 약관 원문이나 내부 업무 매뉴얼
- 내부 시스템 링크나 화면 캡처
- API 키, 로그인 정보, 토큰

## 완료 기준

- `make demo`를 실행했다.
- `make validate` 결과를 확인했다.
- 보험 합성 pack의 CSV와 golden set을 읽었다.
- safety stop과 human handoff가 왜 필요한지 설명할 수 있다.
- 실제 운영 적용 전 필요한 승인 라인을 말할 수 있다.
