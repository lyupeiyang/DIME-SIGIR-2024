import ir_datasets

dataset = ir_datasets.load("msmarco-passage")  # 或者 "msmarco-passage/v2"
for doc in dataset.docs_iter():
    print(doc.doc_id, doc.text)
    count = 0
    for doc in dataset.docs_iter():
        count += 1
    print("Total documents:", count)
