import pytest

from hume import BatchJobStatus


class TestBatchJobStatus:

    def test_update(self):
        # Note: If another status is added to the enum make sure to update parametrized tests below:
        # - test_continuity
        # - test_is_terminal
        assert len(BatchJobStatus) == 4

    @pytest.mark.parametrize("status_str", [
        "COMPLETED",
        "FAILED",
        "IN_PROGRESS",
        "QUEUED",
    ])
    def test_continuity(self, status_str: str):
        assert BatchJobStatus[status_str].value == status_str

    def test_from_str(self):
        assert BatchJobStatus.from_str("COMPLETED") == BatchJobStatus.COMPLETED

    def test_from_str_fail(self):
        with pytest.raises(ValueError, match="Unknown status 'COMPLETE'"):
            BatchJobStatus.from_str("COMPLETE")

    @pytest.mark.parametrize("status,is_terminal", [
        (BatchJobStatus.COMPLETED, True),
        (BatchJobStatus.FAILED, True),
        (BatchJobStatus.IN_PROGRESS, False),
        (BatchJobStatus.QUEUED, False),
    ])
    def test_is_terminal(self, status: BatchJobStatus, is_terminal: bool):
        assert BatchJobStatus.is_terminal(status) == is_terminal