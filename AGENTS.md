# stonecontact-python AI Entry

This repository is the new Python main repository for StoneContact.

Before making changes, always read these knowledge-base docs:

1. `E:\MD工作文档库\Tony工作文档-upload\产品\石联网\03_索引导航\正式需求完成度与优先级-v1.md`
2. `E:\MD工作文档库\Tony工作文档-upload\产品\石联网\03_索引导航\当前对齐完成度与未完成项-v1.md`
3. `E:\MD工作文档库\Tony工作文档-upload\产品\石联网\03_索引导航\Python重建总体架构草案-v1.md`
4. Module-specific review, design, and implementation docs under `03_索引导航`

Current implementation scope:

- Allowed to actively implement: `observability`, `scheduler`, `file_service`, `stats`, `content`, `admin_governance`
- Allowed to scaffold only: `identity`, `company`, `catalog`, `stone_library`, `buyer_rfq`, `message_and_quote`, `seller_service`
- Do not fully implement complex business domains until database/comment review feedback comes back

Rules:

- Any uncertain legacy mapping must be marked as `（不确定）`
- Database, code, and docs must be updated together when structure or business meaning changes
- Do not silently replace old business semantics with cleaner new assumptions

